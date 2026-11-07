import json, soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
k = Kokoro("kokoro.onnx","voices.bin")
lines = json.load(open("script.json"))
out=[]
for i,l in enumerate(lines):
    s,sr = k.create(l, voice="am_michael", speed=1.02, lang="en-us")
    sf.write(f"vo_{i:02d}.wav", s, sr)
    out.append(len(s)/sr)
    print(i, round(len(s)/sr,2), l)
json.dump(out, open("durs.json","w"))
