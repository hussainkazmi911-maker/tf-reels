# usage: python3 sfx.py events.json out.wav total_seconds   (events = [{t,k,v}])  -> synthesized SFX bed, 44.1 kHz mono, peak-limited
import json, sys
import numpy as np
SR = 44100
ev = json.load(open(sys.argv[1])); total = float(sys.argv[3])
buf = np.zeros(int((total + 1) * SR), dtype=np.float64)
rs = np.random.RandomState(4)
def tt(d): return np.arange(int(d * SR)) / SR
def env(n, a=.004, r=.1):
    e = np.ones(n); na = max(1, int(a * SR)); nr = max(1, int(r * SR))
    e[:na] = np.linspace(0, 1, na); e[-nr:] = np.minimum(e[-nr:], np.linspace(1, 0, nr)); return e
def sine(f, d, amp=1): return amp * np.sin(2 * np.pi * f * tt(d))
def sweep(f0, f1, d):
    t = tt(d); f = f0 * (f1 / f0) ** (t / d); return np.sin(2 * np.pi * np.cumsum(f) / SR)
def lp(x, k):  # moving average low-pass
    c = np.cumsum(np.insert(x, 0, 0)); k = int(k)
    y = (c[k:] - c[:-k]) / k; return np.concatenate([np.zeros(k - 1), y])
def pop():
    d = .13; x = sweep(900, 260, d) * np.exp(-tt(d) * 26); return .7 * x
def whoosh():
    d = .42; n = int(d * SR); t = tt(d); x = rs.randn(n); y = lp(x, 6) - lp(x, 60)
    sw = np.sin(np.pi * t / d) ** 1.6; return .55 * y / (np.abs(y).max() + 1e-9) * sw
def ding():
    d = .55; t = tt(d); x = np.sin(2 * np.pi * 1318 * t) + .6 * np.sin(2 * np.pi * 1976 * t) + .25 * np.sin(2 * np.pi * 2637 * t); return .38 * x * np.exp(-t * 7.5) * env(len(t), .002, .05)
def buzz():
    d = .5; t = tt(d); g = (np.sin(2 * np.pi * 14 * t) > 0).astype(float); x = np.sign(np.sin(2 * np.pi * 85 * t)) * .5 + np.sin(2 * np.pi * 170 * t) * .3; return .4 * x * g * env(len(t), .01, .06)
def tick():
    d = .05; x = rs.randn(int(d * SR)) * np.exp(-tt(d) * 150); return .5 * (lp(x, 2) - lp(x, 14))
def coin():
    d = .6; t = tt(d); x = np.sin(2 * np.pi * 1568 * t) * (t < .09) + np.sin(2 * np.pi * 2093 * t) * (t >= .09) ; return .35 * x * np.exp(-np.maximum(t - .09, 0) * 6) * env(len(t), .002, .05) + .12 * np.sin(2 * np.pi * 4186 * t) * np.exp(-t * 9)
def success():
    out = np.zeros(int(.7 * SR))
    for i, f in enumerate([523.25, 659.25, 783.99]):
        n = int((.5) * SR); t = np.arange(n) / SR; x = (np.sin(2 * np.pi * f * t) + .3 * np.sin(2 * np.pi * 2 * f * t)) * np.exp(-t * 6) * env(n, .003, .05) * .28
        o = int(i * .07 * SR); out[o:o + n] += x[:len(out) - o]
    return out
def stamp():
    d = .3; t = tt(d); x = np.sin(2 * np.pi * 62 * t) * np.exp(-t * 14) + .6 * lp(rs.randn(len(t)), 8) * np.exp(-t * 30); return .85 * x
def zap():
    d = .32; x = sweep(220, 1500, d); return .3 * x * env(len(x), .005, .12)
def neon():
    d = .5; t = tt(d); g = (np.sin(2 * np.pi * 22 * t + 1) > -.2).astype(float); return .25 * (np.sin(2 * np.pi * 120 * t) + .5 * np.sign(np.sin(2 * np.pi * 120 * t))) * g * env(len(t), .01, .15)
def typ():
    d = .035; x = rs.randn(int(d * SR)) * np.exp(-tt(d) * 220); return .35 * (lp(x, 2) - lp(x, 10))
FN = dict(pop=pop, whoosh=whoosh, ding=ding, buzz=buzz, tick=tick, coin=coin, success=success, stamp=stamp, zap=zap, neon=neon, type=typ)
for e in ev:
    f = FN.get(e['k'])
    if not f: continue
    x = f() * e.get('v', 1); o = int(max(0, e['t']) * SR); n = min(len(x), len(buf) - o)
    if n > 0: buf[o:o + n] += x[:n]
pk = np.abs(buf).max(); buf = buf / pk * min(1, .9) if pk > .9 else buf
import wave
w = wave.open(sys.argv[2], 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((buf * 32767).astype(np.int16).tobytes()); w.close()
print('sfx', len(ev), 'events ->', sys.argv[2])
