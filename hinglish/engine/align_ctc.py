# usage (run inside work/rNN): python3 ../../engine/align_ctc.py voice.mp3 ../../episodes/rNN.json
# Whole-file CTC forced alignment of the script text against the real TTS take -> timing.json / timing.js.
import json, re, subprocess, sys, os
AUDIO = sys.argv[1] if len(sys.argv) > 1 else 'voice.mp3'
EPF = sys.argv[2]
lines = [l.split() for l in json.load(open(EPF))['lines']]
dur = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',AUDIO]).decode())
_o = subprocess.run(['ffmpeg','-hide_banner','-i',AUDIO,'-af','silencedetect=noise=-35dB:d=0.12','-f','null','-'],capture_output=True,text=True).stderr
sil = list(zip([float(x) for x in re.findall(r'silence_start: ([\d.]+)', _o)], [float(x) for x in re.findall(r'silence_end: ([\d.]+)', _o)]))
LEAD = 0.2   # audio is delayed by this in the mux so the first word doesn't clip
# model: https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-nemo-ctc-en-conformer-small.tar.bz2 -> models/model.int8.onnx (tokens: models/ctc_tokens.txt)
import numpy as np, librosa, onnxruntime as ort
SR = 16000; STRIDE = 0.04
HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.environ.get('CTC_MODEL', os.path.join(HERE, 'models', 'model.int8.onnx'))
TOKS = [l.split()[0] for l in open(os.path.join(HERE, 'models', 'ctc_tokens.txt'))]
TID = {t: i for i, t in enumerate(TOKS)}; BLANK = len(TOKS) - 1
if not os.path.exists(MODEL):   # fetch the model once (76 MB archive, ~46 MB model)
    import urllib.request, tarfile, io
    URL = 'https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-nemo-ctc-en-conformer-small.tar.bz2'
    os.makedirs(os.path.dirname(MODEL), exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(urllib.request.urlopen(URL).read()), mode='r:bz2') as tf:
        open(MODEL, 'wb').write(tf.extractfile('sherpa-onnx-nemo-ctc-en-conformer-small/model.int8.onnx').read())
sess = ort.InferenceSession(MODEL)
y, _ = librosa.load(AUDIO, sr=SR, mono=True)
MEL = librosa.filters.mel(sr=SR, n_fft=512, n_mels=80, fmin=0, fmax=8000, norm='slaney')
def feats(x):
    x = np.concatenate([[x[0]], x[1:] - 0.97 * x[:-1]]).astype(np.float32)
    P = np.abs(librosa.stft(x, n_fft=512, hop_length=160, win_length=400, window='hann', center=True, pad_mode='reflect')) ** 2
    X = np.log(MEL @ P + 2 ** -24)
    return ((X - X.mean(1, keepdims=True)) / (X.std(1, ddof=1, keepdims=True) + 1e-5)).astype(np.float32)
def logprobs(x):
    f = feats(x)
    return sess.run(None, {'audio_signal': f[None], 'length': np.array([f.shape[1]], dtype=np.int64)})[0][0]
SP = '\u2581'
def tokenize(word):
    w = re.sub(r"[^a-z']", '', word.lower()) or 'a'
    out = []; i = 0
    while i < len(w):
        for j in range(len(w), i, -1):
            p = (SP if i == 0 else '') + w[i:j]
            if p in TID: out.append(TID[p]); i = j; break
        else:
            if i == 0 and SP in TID: out.append(TID[SP])
            i += 1
    return out or [TID.get(SP + 'a', 3)]
def ctc_align(lp, seq):
    T = lp.shape[0]; N = len(seq); S = 2 * N + 1
    ext = np.full(S, BLANK); ext[1::2] = seq
    skip = np.zeros(S, bool); skip[3::2] = ext[3::2] != ext[1:-2:2]
    NEG = -1e30; dp = np.full((T, S), NEG); bp = np.zeros((T, S), np.int8)
    dp[0, 0] = lp[0, BLANK]; dp[0, 1] = lp[0, ext[1]]
    for t in range(1, T):
        p0 = dp[t - 1]; p1 = np.concatenate([[NEG], p0[:-1]]); p2 = np.concatenate([[NEG, NEG], p0[:-2]]); p2 = np.where(skip, p2, NEG)
        c = np.stack([p0, p1, p2]); k = c.argmax(0); dp[t] = c[k, np.arange(S)] + lp[t, ext]; bp[t] = k
    s = S - 1 if dp[T - 1, S - 1] >= dp[T - 1, S - 2] else S - 2
    path = np.zeros(T, int)
    for t in range(T - 1, -1, -1):
        path[t] = s; s -= int(bp[t, s])
    return path
allw = [w for L in lines for w in L]
toks = [tokenize(w) for w in allw]; flat = [t for ts in toks for t in ts]
lp = logprobs(y)
assert lp.shape[0] >= len(flat) * 1.05 + 2, 'audio too short for the script text'
path = ctc_align(lp, flat)
fr = {}
for t, s in enumerate(path):
    if s % 2 == 1: fr.setdefault((s - 1) // 2, []).append(t)
W = []; n = 0
for i, w in enumerate(allw):
    idx = [j for j in range(n, n + len(toks[i])) if j in fr]; n += len(toks[i])
    W.append([min(fr[j][0] for j in idx) * STRIDE, (max(fr[j][-1] for j in idx) + 1) * STRIDE])
# monotonic, minimum length
last = 0.0
for i in range(len(W)):
    W[i][0] = max(W[i][0], last); W[i][1] = max(W[i][1], W[i][0] + .06); last = W[i][0] + .04
# snap word starts / ends to real pauses (>= 0.12 s) when within 0.2 s
for a, b in sil:
    cand = [i for i in range(1, len(W)) if abs(W[i][0] - b) < .2]
    if not cand: continue
    i = min(cand, key=lambda i: abs(W[i][0] - b)); W[i][0] = b
    if abs(W[i - 1][1] - a) < .2 and a > W[i - 1][0] + .05: W[i - 1][1] = a
for i in range(len(W)):
    if i and W[i][0] < W[i - 1][0] + .04: W[i][0] = W[i - 1][0] + .04
    if W[i][1] < W[i][0] + .05: W[i][1] = W[i][0] + .05
res = []; n = 0
for k, L in enumerate(lines):
    words = [{'w': w, 's': round(W[n + i][0] + LEAD, 3), 'e': round(W[n + i][1] + LEAD, 3)} for i, w in enumerate(L)]; n += len(L)
    res.append({'start': words[0]['s'], 'end': words[-1]['e'], 'words': words})
    print(k, res[-1]['start'], res[-1]['end'], '|', ' '.join(L)[:44])
T = {'total': round(dur + LEAD + 0.5, 3), 'lead': LEAD, 'lines': res, 'audio': AUDIO}
json.dump(T, open('timing.json', 'w'), indent=1)
open('timing.js', 'w').write('window.TIMING=' + json.dumps(T) + ';')
print('total', T['total'])
