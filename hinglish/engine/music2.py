# usage: python3 music2.py out.wav seconds [bpm] -> quiet original music bed (A minor: Am F C G), soft pad + sub + pluck arp + faint hats. Original, synthesized here.
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; dur = float(sys.argv[2]); bpm = float(sys.argv[3]) if len(sys.argv) > 3 else 98
n = int(dur * SR); out = np.zeros(n + SR * 4); beat = 60 / bpm; bar = 4 * beat; rs = np.random.RandomState(3)
def lpf(x, f, o=2): return sosfilt(butter(o, f, btype='low', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, btype='high', fs=SR, output='sos'), x)
def add(x, t0):
    o = int(t0 * SR)
    if o >= len(out): return
    m = min(len(x), len(out) - o); out[o:o + m] += x[:m]
mid = lambda m: 440 * 2 ** ((m - 69) / 12)
CH = [([57, 60, 64], 33), ([53, 57, 60], 29), ([60, 64, 67], 36), ([55, 59, 62], 31)]   # chord tones, bass note
def env_ar(d, a, r):
    k = int(d * SR); e = np.ones(k); na = int(a * SR); nr = int(r * SR); e[:na] = np.linspace(0, 1, na); e[-nr:] = np.minimum(e[-nr:], np.linspace(1, 0, nr)); return e
nb = int(dur / bar) + 2
for b in range(nb):
    t0 = b * bar; notes, bass = CH[b % 4]
    t = np.arange(int(bar * 1.15 * SR)) / SR
    pad = sum(np.sin(2 * np.pi * mid(m) * (1 + d) * t) + .4 * np.sin(2 * np.pi * 2 * mid(m) * (1 - d) * t) for m in notes for d in (-.0035, 0, .0035))
    pad = lpf(pad, 1400) * env_ar(bar * 1.15, .7, .9) * .028; add(pad, t0)
    for k, (bt, ln) in enumerate([(0, 1.8), (2, 1.2), (3.5, .5)]):                     # sub bass: beats 1, 3 and a pickup
        d = ln * beat; tb = np.arange(int(d * SR)) / SR; f = mid(bass)
        x = (np.sin(2 * np.pi * f * tb) + .25 * np.sin(2 * np.pi * 2 * f * tb)) * np.exp(-tb * 3.2) * env_ar(d, .005, .08); add(.2 * x, t0 + bt * beat)
    for k in range(8):                                                                   # plucked arp, 8th notes
        m = notes[[0, 1, 2, 1, 2, 1, 0, 1][k]] + 12; d = .5; tp = np.arange(int(d * SR)) / SR
        x = lpf(np.sin(2 * np.pi * mid(m) * tp) + .35 * np.sin(2 * np.pi * 2 * mid(m) * tp), 3800) * np.exp(-tp * 9) * env_ar(d, .004, .1); add(.05 * x, t0 + k * beat / 2)
    for k in range(8):                                                                   # faint offbeat hats
        d = .05; th = np.arange(int(d * SR)) / SR; x = hp(rs.randn(len(th)), 7500) * np.exp(-th * 90); add(.02 * x * (1 if k % 2 else .5), t0 + k * beat / 2 + (beat / 4 if k % 2 else 0))
    for bt in (0, 2):                                                                    # soft kick
        d = .25; tk = np.arange(int(d * SR)) / SR; f = 52 + 60 * np.exp(-tk * 30); x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tk * 11); add(.16 * x, t0 + bt * beat)
x = out[:n]; fi = int(1.0 * SR); fo = int(1.6 * SR); x[:fi] *= np.linspace(0, 1, fi); x[-fo:] *= np.linspace(1, 0, fo)
x = x / (np.abs(x).max() + 1e-9) * .8
w = wave.open(sys.argv[1], 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype(np.int16).tobytes()); w.close()
print('music', dur, 's ->', sys.argv[1])
