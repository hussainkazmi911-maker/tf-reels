# usage: python3 sheet_all.py out_prefix r03 r04 ... -> out_prefix_N.png (3 episodes per image, 9 scenes each at the 75% mark of the scene)
import sys, glob
from PIL import Image
pre = sys.argv[1]; eps = sys.argv[2:]; w, h = 160, 284
for n in range(0, len(eps), 3):
    grp = eps[n:n + 3]; S = Image.new('RGB', (9 * w, len(grp) * h), 'black')
    for r, e in enumerate(grp):
        fs = sorted(glob.glob(f'/home/claude/tf-reels/hinglish/work/{e}/dense/f_*.png'))
        for i in range(9): S.paste(Image.open(fs[i * 6 + 4]).resize((w, h)), (i * w, r * h))
    S.save(f'{pre}_{n // 3 + 1}.png')
print('ok')
