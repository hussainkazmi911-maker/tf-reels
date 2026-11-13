#!/bin/bash
# needs: pip install librosa onnxruntime (aligner = CTC forced alignment with an ONNX conformer, model auto-downloads to engine/models; align_dtw.py / align_ep.py are older fallbacks)
# usage: engine/finish_ep.sh rNN /path/voice.mp3 slug   -> align, render 1080x1920 (2 workers), mux, write reels/hinglish_rNN_slug.mp4
set -e
ID=$1; AUD=$2; SLUG=$3
H=/home/claude/tf-reels/hinglish
cd $H/work/$ID
cp "$AUD" voice.mp3
python3 $H/engine/align_ctc.py voice.mp3 $H/episodes/$ID.json
rm -rf frames
python3 render.py run 2 0 > r0.log 2>&1 &
python3 render.py run 2 1 > r1.log 2>&1 &
wait
cat r0.log r1.log
ffmpeg -y -hide_banner -loglevel error -framerate 30 -i frames/f_%05d.png -i voice.mp3 -filter_complex "[1:a]adelay=200|200[a]" -map 0:v -map "[a]" -c:v libx264 -preset veryfast -crf 23 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart $H/../reels/hinglish_${ID}_${SLUG}.mp4
ls -la $H/../reels/hinglish_${ID}_${SLUG}.mp4
