# usage: python3 csheet.py sNN out_prefix  -> contact sheets from work/sNN/test (3 frames per scene; uses frames 2 and 3), 4 scenes per image
import sys, glob, os
from PIL import Image
k, outp = sys.argv[1], sys.argv[2]
fs = sorted(glob.glob(f'work/{k}/test/f_*.png'))
n = len(fs) // 3
W, Hh = 300, 533
for part in range(0, n, 4):
    sc = list(range(part, min(n, part + 4)))
    im = Image.new('RGB', (W * len(sc), Hh * 2), '#222')
    for ci, s in enumerate(sc):
        for r, fi in enumerate((1, 2)):
            im.paste(Image.open(fs[s * 3 + fi]).resize((W, Hh)), (ci * W, r * Hh))
    im.save(f'{outp}_{part // 4}.png')
print(n, 'scenes')
