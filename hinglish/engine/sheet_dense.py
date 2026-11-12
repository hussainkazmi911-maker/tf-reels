# usage: python3 sheet_dense.py out_prefix rNN [scenes_per_sheet=3] -> out_prefix_1.png ...  (rows = scenes, 6 frames each, from work/rNN/dense)
import sys, glob
from PIL import Image
pre, e = sys.argv[1], sys.argv[2]; per = int(sys.argv[3]) if len(sys.argv) > 3 else 3
w, h = 200, 356
fs = sorted(glob.glob(f'/home/claude/tf-reels/hinglish/work/{e}/dense/f_*.png'))
# frames are saved in ascending frame number which matches scene order
n = len(fs) // 6
for sh in range(0, n, per):
    rows = min(per, n - sh)
    S = Image.new('RGB', (6 * w, rows * h), 'black')
    for r in range(rows):
        for c in range(6):
            S.paste(Image.open(fs[(sh + r) * 6 + c]).resize((w, h)), (c * w, r * h))
    S.save(f'{pre}_{sh // per + 1}.png')
print('sheets', (n + per - 1) // per)
