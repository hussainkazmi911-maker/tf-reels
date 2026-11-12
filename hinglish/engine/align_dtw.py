# usage (run inside work/rNN): python3 ../../engine/align_ep.py voice.mp3 ../../episodes/rNN.json
# Build real word timings from a single TTS take: silence-detect, pick 8 line boundaries by DP, spread words by letter weight inside speech only.
import json, re, subprocess, itertools, sys
AUDIO = sys.argv[1] if len(sys.argv) > 1 else 'voice.mp3'
EPF = sys.argv[2]
S = {'lines': [{'words': l.split()} for l in json.load(open(EPF))['lines']]}
dur = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',AUDIO]).decode())
out = subprocess.run(['ffmpeg','-hide_banner','-i',AUDIO,'-af','silencedetect=noise=-35dB:d=0.28','-f','null','-'],capture_output=True,text=True).stderr
st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', out)]
en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', out)]
sil = list(zip(st, en))
# speech segments
seg = []; t = 0.0
for a, b in sil:
    if a - t > 0.05: seg.append([t, a])
    t = b
if dur - t > 0.05: seg.append([t, dur])
# trim trailing: last segment end = dur
lines = [[w for w in L['words']] for L in S['lines']]
wl = lambda w: max(1, len(re.sub(r'[^A-Za-z]', '', w))) + 0.6   # weight
LW = [sum(wl(w) for w in L) for L in lines]
speech_total = sum(b - a for a, b in seg)
tot = sum(LW)
# expected cumulative speech-time at each line end
exp_end = list(itertools.accumulate(LW)); exp_end = [e / tot * speech_total for e in exp_end]
# speech-time position of the middle of each silence (cumulative speech time before it)
def spos(x):
    p = 0
    for a, b in seg:
        if b <= x: p += b - a
        elif a < x: p += x - a
    return p
cand = [(a, b, spos((a + b) / 2), b - a) for a, b in sil]
# DP: choose 8 boundaries in order minimizing sum (spos - exp_end)^2 - bonus*duration
import math
n = len(cand)
best = {}
def solve(k, i):
    if k == 8: return 0, []
    if i >= n: return math.inf, []
    key = (k, i)
    if key in best: return best[key]
    r = (math.inf, [])
    for j in range(i, n):
        c = (cand[j][2] - exp_end[k]) ** 2 - 6 * cand[j][3]
        s, rest = solve(k + 1, j + 1)
        if c + s < r[0]: r = (c + s, [j] + rest)
    best[key] = r
    return r
cost, pick = solve(0, 0)
bounds = [cand[j] for j in pick]
print('boundaries (s):', [(round(b[0],2), round(b[1],2)) for b in bounds])
# line spans
spans = []
prev_end = seg[0][0]
for k in range(9):
    ls = prev_end
    le = bounds[k][0] if k < 8 else seg[-1][1]
    spans.append((ls, le))
    if k < 8: prev_end = bounds[k][1]
LEAD = 0.2   # audio is delayed by this in the mux so the first word doesn't clip
# ---- DTW forced alignment: synthesise each line with espeak-ng (word boundaries known), DTW its MFCCs against the real take
import os, ctypes, numpy as np, librosa, espeakng_loader
SR = 16000
y, _ = librosa.load(AUDIO, sr=SR, mono=True)
lib = ctypes.CDLL(espeakng_loader.get_library_path())
CB = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_short), ctypes.c_int, ctypes.c_void_p)
_buf = []
def _cb(wav, n, ev):
    if wav and n > 0: _buf.append(np.ctypeslib.as_array(wav, shape=(n,)).copy())
    return 0
_cbref = CB(_cb)
lib.espeak_Initialize.restype = ctypes.c_int
ESR = lib.espeak_Initialize(2, 0, os.path.dirname(espeakng_loader.get_data_path()).encode(), 0)
lib.espeak_SetSynthCallback(_cbref); lib.espeak_SetVoiceByName(b'en-us')
def synth(text, rate):
    _buf.clear(); lib.espeak_SetParameter(1, int(rate), 0)
    b = text.encode('utf-8'); lib.espeak_Synth(b, len(b) + 1, 0, 0, 0, 1, None, None); lib.espeak_Synchronize()
    a = np.concatenate(_buf).astype(np.float32) / 32768 if _buf else np.zeros(160, np.float32)
    a = librosa.resample(a, orig_sr=ESR, target_sr=SR)
    nz = np.where(np.abs(a) > 0.012)[0]
    return a[nz[0]:nz[-1] + 1] if len(nz) else a
def clean(w):
    c = re.sub(r"[^A-Za-z0-9']", ' ', w).strip()
    return c if c else 'a'
def build_ref(ws, rate):
    segs = []; marks = []; t = 0
    for w in ws:
        a = synth(clean(w), rate)
        gap = int(SR * (0.22 if re.search(r'[,.?:!]$', w) else 0.04))
        marks.append((t / SR, (t + len(a)) / SR)); segs.append(a); segs.append(np.zeros(gap, np.float32)); t += len(a) + gap
    return np.concatenate(segs), marks
def feats(x):
    m = librosa.feature.mfcc(y=x, sr=SR, n_mfcc=13, n_fft=400, hop_length=160, n_mels=40, fmax=7600)
    m[0] = (m[0] - m[0].mean()) / (m[0].std() + 1e-6) * 3
    m[1:] = m[1:] - m[1:].mean(axis=1, keepdims=True)
    d = librosa.feature.delta(m[1:], width=5)
    return np.vstack([m, d * .6])
HOP = 160 / SR
res = []; MARG = 0.06
for k, (ls, le) in enumerate(spans):
    ws = lines[k]
    sg = [[max(a, ls), min(b, le)] for a, b in seg if b > ls and a < le]
    real_speech = sum(b - a for a, b in sg)
    rate = 175
    ref, marks = build_ref(ws, rate)
    refspeech = sum(e - s for s, e in marks) + 0.04 * len(ws)
    rate = float(np.clip(rate * refspeech / max(real_speech, .3), 90, 420))
    ref, marks = build_ref(ws, rate)
    t0 = max(0.0, ls - MARG); x = y[int(t0 * SR):int((le + MARG) * SR)]
    X = feats(ref); Y = feats(x)
    D, wp = librosa.sequence.dtw(X=X, Y=Y, metric='euclidean')
    wp = wp[::-1]
    jmin = {}; jmax = {}
    for i, j in wp:
        jmin.setdefault(int(i), int(j)); jmax[int(i)] = int(j)
    nref = X.shape[1] - 1
    words = []; last = -1.0
    for i, w in enumerate(ws):
        a, b = marks[i]; ia = min(nref, int(a / HOP)); ib = min(nref, max(ia, int(b / HOP) - 1))
        s0 = t0 + jmin[ia] * HOP; s1 = t0 + jmax[ib] * HOP
        s0 = max(s0, last); s1 = max(s1, s0 + .06); last = s1
        words.append({'w': w, 's': round(s0 + LEAD, 3), 'e': round(s1 + LEAD, 3)})
    # snap word edges to real pauses (>=0.28 s) when DTW put them within 0.22 s of one
    for a, b in sil:
        if b < ls or a > le: continue
        cand = [i for i, w in enumerate(words) if i > 0 and abs(w['s'] - LEAD - b) < .22]
        if not cand: continue
        i = min(cand, key=lambda i: abs(words[i]['s'] - LEAD - b))
        words[i]['s'] = round(b + LEAD, 3)
        if abs(words[i - 1]['e'] - LEAD - a) < .22: words[i - 1]['e'] = round(a + LEAD, 3)
    for i in range(len(words)):
        if i and words[i]['s'] < words[i - 1]['s'] + .04: words[i]['s'] = round(words[i - 1]['s'] + .04, 3)
        if words[i]['e'] < words[i]['s'] + .05: words[i]['e'] = round(words[i]['s'] + .05, 3)
    res.append({'start': round(ls + LEAD, 3), 'end': round(le + LEAD, 3), 'words': words})
    print(k, round(ls + LEAD, 2), round(le + LEAD, 2), 'rate', int(rate), 'cost/frame', round(float(D[-1, -1]) / len(wp), 2), '|', ' '.join(ws)[:40])
T = {'total': round(dur + LEAD + 0.5, 3), 'lead': LEAD, 'lines': res, 'audio': AUDIO}
json.dump(T, open('timing.json', 'w'), indent=1)
open('timing.js', 'w').write('window.TIMING=' + json.dumps(T) + ';')
print('total', T['total'])
for L in res[1:2]:
    print([(w['w'], w['s'], w['e']) for w in L['words']])
