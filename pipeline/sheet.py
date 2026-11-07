# usage (inside day work dir): python3 sheet.py  -> test/sheet0.png ... (6 frames per sheet, 1620px wide)
import glob
from PIL import Image
fs=sorted(glob.glob('test/f_*.png'))
for n in range(0,len(fs),6):
    ims=[Image.open(f).resize((270,480)) for f in fs[n:n+6]]
    sh=Image.new('RGB',(270*len(ims),480))
    for i,im in enumerate(ims): sh.paste(im,(270*i,0))
    sh.save(f'test/sheet{n//6}.png')
print(len(fs),'frames ->',(len(fs)+5)//6,'sheets')
