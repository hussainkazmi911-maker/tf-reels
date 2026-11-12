# Build real word timings from a single TTS take: silence-detect, pick 8 line boundaries by DP, spread words by letter weight inside speech only.
import json, re, subprocess, itertools, sys
AUDIO = sys.argv[1] if len(sys.argv) > 1 else 'voice.mp3'
S = json.load(open('script.json'))
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
res = []
for k, (ls, le) in enumerate(spans):
    sg = [[max(a, ls), min(b, le)] for a, b in seg if b > ls and a < le]
    ws = lines[k]; W = [wl(w) for w in ws]; tw = sum(W)
    # phrases split after punctuation
    ph = []; cur = []
    for i, w in enumerate(ws):
        cur.append(i)
        if re.search(r'[,.?:!]$', w) and i < len(ws) - 1: ph.append(cur); cur = []
    ph.append(cur)
    P = len(ph); K = len(sg)
    pw = [sum(W[i] for i in p) for p in ph]
    cumw = list(itertools.accumulate(pw))
    segd = [b - a for a, b in sg]; cums = list(itertools.accumulate(segd))
    # choose K-1 of P-1 phrase boundaries to coincide with the K-1 internal silences
    if K > 1:
        bestc, bestc_pick = math.inf, None
        for comb in itertools.combinations(range(P - 1), min(K - 1, P - 1)):
            c = sum((cumw[j] / tw - cums[m] / cums[-1]) ** 2 for m, j in enumerate(comb))
            if c < bestc: bestc, bestc_pick = c, comb
        cut = list(bestc_pick) + [P - 1]
    else:
        cut = [P - 1]
    words = [None] * len(ws)
    p0 = 0
    for m, cj in enumerate(cut):
        if m >= len(sg): break
        idx = [i for p in ph[p0:cj + 1] for i in p]
        a, b = sg[m]
        wsum = sum(W[i] for i in idx); c = 0
        for i in idx:
            s0 = a + (b - a) * c / wsum; c += W[i]; s1 = a + (b - a) * c / wsum
            words[i] = {'w': ws[i], 's': round(s0 + LEAD, 3), 'e': round(s1 + LEAD, 3)}
        p0 = cj + 1
    for i in range(len(words)):
        if words[i] is None:   # leftover safety
            prev = words[i - 1]['e'] if i else ls + LEAD
            words[i] = {'w': ws[i], 's': prev, 'e': round(prev + .25, 3)}
    res.append({'start': round(ls + LEAD, 3), 'end': round(le + LEAD, 3), 'words': words})
    print(k, round(ls + LEAD, 2), round(le + LEAD, 2), 'segs', K, 'phrases', P, '|', ' '.join(ws)[:38])
T = {'total': round(dur + LEAD + 0.5, 3), 'lead': LEAD, 'lines': res, 'audio': AUDIO}
json.dump(T, open('timing.json', 'w'), indent=1)
open('timing.js', 'w').write('window.TIMING=' + json.dumps(T) + ';')
print('total', T['total'])
for L in res[1:2] + res[5:6]:
    print([(w['w'], w['s'], w['e']) for w in L['words']])
