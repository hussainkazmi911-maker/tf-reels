#!/bin/bash
# usage: engine/qa_v2.sh file.mp4 sheet.png -> duration, loudness, streams, contact sheet of 12 frames
F=$1; S=$2
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,duration -of compact $F
ffmpeg -hide_banner -nostats -i $F -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I:|LRA:|Peak:)"
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $F)
rm -rf /tmp/qa_$$; mkdir /tmp/qa_$$
for i in $(seq 0 11); do T=$(python3 -c "print(round(($i+.5)*$D/12,2))"); ffmpeg -y -hide_banner -loglevel error -ss $T -i $F -frames:v 1 -vf scale=240:-1 /tmp/qa_$$/f$(printf %02d $i).png; done
python3 - <<PY
from PIL import Image
import glob
fs=sorted(glob.glob('/tmp/qa_$$/f*.png')); ims=[Image.open(f) for f in fs]; w,h=ims[0].size
s=Image.new('RGB',(w*6,h*2))
for k,im in enumerate(ims): s.paste(im,((k%6)*w,(k//6)*h))
s.save('$S')
PY
rm -rf /tmp/qa_$$
