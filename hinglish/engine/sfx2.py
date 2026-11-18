# usage: python3 sfx2.py events.json out.wav total_seconds -> clean, soft UI sound design (original, synthesized). kinds: pop tick whoosh swell ding success stamp type
import json, sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100
ev = json.load(open(sys.argv[1])); total = float(sys.argv[3])
buf = np.zeros(int((total + 1.5) * SR)); rs = np.random.RandomState(7)
tt = lambda d: np.arange(int(d * SR)) / SR
def bp(x, lo, hi, o=2):
    return sosfilt(butter(o, [lo, hi], btype='band', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, btype='high', fs=SR, output='sos'), x)
def lpf(x, f, o=2): return sosfilt(butter(o, f, btype='low', fs=SR, output='sos'), x)
def sw(f0, f1, d): t = tt(d); f = f0 * (f1 / f0) ** (t / d); return np.sin(2 * np.pi * np.cumsum(f) / SR)
def pop():
    d = .16; t = tt(d); x = sw(760, 420, d) * np.exp(-t * 30); c = hp(rs.randn(len(t)), 2500) * np.exp(-t * 400) * .15; return .5 * (x + c)
def tick():
    d = .08; t = tt(d); return .28 * (np.sin(2 * np.pi * 2900 * t) + .5 * np.sin(2 * np.pi * 4350 * t)) * np.exp(-t * 85)
def whoosh():
    d = .55; t = tt(d); n = rs.randn(len(t)); x = bp(n, 700, 7000) ; env = np.minimum(1, t / .16) ** 2 * np.exp(-np.maximum(t - .16, 0) * 7)
    return .55 * x / (np.abs(x).max() + 1e-9) * env
def swell():
    d = .85; t = tt(d); n = rs.randn(len(t)); x = bp(n, 350, 4200); env = (t / d) ** 2.2 * np.exp(-np.maximum(t - .75, 0) * 30)
    tone = np.sin(2 * np.pi * np.cumsum(180 * (3 ** (t / d))) / SR) * .25
    return .4 * (x / (np.abs(x).max() + 1e-9) * .8 + tone) * env
def bell(freqs, d, amps, dec):
    t = tt(d); return sum(a * np.sin(2 * np.pi * f * t) * np.exp(-t * dec * (1 + i * .5)) for i, (f, a) in enumerate(zip(freqs, amps)))
def ding(): return .32 * bell([1175, 1760, 2349], .7, [1, .5, .22], 6)
def success():
    out = np.zeros(int(.9 * SR))
    for i, f in enumerate([523.25, 659.25, 783.99, 1046.5]):
        x = .26 * bell([f, 2 * f], .6, [1, .3], 7); o = int(i * .075 * SR); out[o:o + len(x)] += x[:len(out) - o]
    return out
def stamp():
    d = .35; t = tt(d); return .9 * (sw(110, 42, d) * np.exp(-t * 11) + .5 * lpf(rs.randn(len(t)), 900) * np.exp(-t * 38))
def typ():
    d = .05; t = tt(d); return .3 * hp(rs.randn(len(t)), 3500) * np.exp(-t * 130)
FN = dict(pop=pop, tick=tick, whoosh=whoosh, swell=swell, ding=ding, success=success, stamp=stamp, type=typ)
for e in ev:
    f = FN.get(e['k'])
    if not f: continue
    x = f() * e.get('v', 1); o = int(max(0, e['t']) * SR); n = min(len(x), len(buf) - o)
    if n > 0: buf[o:o + n] += x[:n]
pk = np.abs(buf).max(); buf = buf / pk * .85 if pk > .85 else buf
w = wave.open(sys.argv[2], 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((buf * 32767).astype(np.int16).tobytes()); w.close()
print('sfx', len(ev), 'events ->', sys.argv[2])
