# usage: python3 sheet_end.py out.png r03 r04 ...  -> one row per episode, last test frame of each of the 9 scenes
import sys, glob
from PIL import Image
w, h = 220, 391
eps = sys.argv[2:]
S = Image.new('RGB', (9 * w, len(eps) * h), 'black')
for r, e in enumerate(eps):
    fs = sorted(glob.glob(f'/home/claude/tf-reels/hinglish/work/{e}/test/f_*.png'))
    for i in range(9):
        S.paste(Image.open(fs[i * 3 + 2]).resize((w, h)), (i * w, r * h))
S.save(sys.argv[1]); print(S.size)
