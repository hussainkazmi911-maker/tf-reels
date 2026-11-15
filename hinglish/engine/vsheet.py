# usage: python3 vsheet.py reel.mp4 out.png [t1 t2 ...]  -> contact sheet of frames
import sys, subprocess, os
from PIL import Image
mp4, out = sys.argv[1], sys.argv[2]
ts = [float(x) for x in sys.argv[3:]] or [1.5, 5, 8, 11, 14, 18, 21.5, 25]
ims = []
for i, t in enumerate(ts):
    f = f'/tmp/_vs_{os.getpid()}_{i}.png'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(t), '-i', mp4, '-frames:v', '1', '-vf', 'scale=300:-1', f], check=True)
    ims.append(Image.open(f))
w, h = ims[0].size; cols = 4; rows = (len(ims) + cols - 1) // cols
S = Image.new('RGB', (w * cols, h * rows))
for i, im in enumerate(ims): S.paste(im, ((i % cols) * w, (i // cols) * h))
S.save(out)
