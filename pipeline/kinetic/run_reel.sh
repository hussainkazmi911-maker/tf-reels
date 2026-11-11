#!/bin/bash
# usage: bash pipeline/kinetic/run_reel.sh rNN [full]   -> work dir /home/claude/forge/rNN ; test sheet always; 'full' renders + encodes out.mp4
set -e
R=$1; REPO=$(cd "$(dirname "$0")/../.." && pwd); K=$REPO/pipeline/kinetic; W=/home/claude/forge/$R
mkdir -p $W && cd $W && ln -sf /home/claude/forge/node_modules node_modules && cp /home/claude/forge/logo.png .
cp $K/engine.js $K/kinetic.css $K/build_k.py $K/render_k.py $K/mkaudio_k.py . && cp $REPO/brand/$R/reel.json .
python3 build_k.py && python3 mkaudio_k.py ${VOICE:+$VOICE}
rm -rf test && python3 render_k.py test
python3 - <<'PY'
import glob
from PIL import Image
fs=sorted(glob.glob('test/f_*.png'))
for n in range(0,len(fs),8):
    ims=[Image.open(f).resize((250,444)) for f in fs[n:n+8]]
    sh=Image.new('RGB',(250*len(ims),444))
    for i,im in enumerate(ims): sh.paste(im,(250*i,0))
    sh.save(f'test/sheet{n//8}.png')
PY
if [ "$2" = "full" ]; then
  T=$(python3 -c "import json;print(int(sum(b['d'] for b in json.load(open('reel.json'))['beats'])*30)+1)")
  rm -rf frames; mkdir frames
  for k in 0 1; do python3 render_k.py run 2 $k > r$k.log 2>&1 & done; wait
  ffmpeg -y -loglevel error -framerate 30 -i frames/f_%05d.png -i mix.wav -vf "scale=1080:1920:flags=lanczos" -c:v libx264 -preset veryfast -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart out.mp4
  ffprobe -v error -show_entries format=duration,size -of default=nw=1 out.mp4
fi
