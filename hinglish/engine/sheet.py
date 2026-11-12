# usage: python3 sheet.py rNN  -> work/rNN/sheet.png (3 rows x 9 cols from test/)
import sys, glob, os
from PIL import Image
d = f'/home/claude/tf-reels/hinglish/work/{sys.argv[1]}/test'
fs = sorted(glob.glob(d + '/f_*.png'))
w, h = 240, 427
cols = 9; rows = (len(fs) + cols - 1) // cols
S = Image.new('RGB', (cols * w, rows * h), 'black')
for i, f in enumerate(fs):
    S.paste(Image.open(f).resize((w, h)), ((i % cols) * w, (i // cols) * h))
S.save(f'/home/claude/tf-reels/hinglish/work/{sys.argv[1]}/sheet.png')
print(len(fs), S.size)
