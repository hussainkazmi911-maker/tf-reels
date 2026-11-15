#!/bin/bash
# usage: engine/mux_story.sh sNN slug  (after frames/ is rendered and work/sNN/sfx.wav exists) -> reels/hinglish_sNN_slug.mp4
set -e
ID=$1; SLUG=$2; H=/home/claude/tf-reels/hinglish
cd $H/work/$ID
ffmpeg -y -hide_banner -loglevel error -framerate 30 -i frames/f_%05d.png -i voice.mp3 -i sfx.wav \
 -filter_complex "[1:a]adelay=200|200[v];[2:a]volume=0.30[s];[v][s]amix=inputs=2:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=9[a]" \
 -map 0:v -map "[a]" -c:v libx264 -preset veryfast -crf 22 -pix_fmt yuv420p -c:a aac -b:a 160k -shortest -movflags +faststart $H/../reels/hinglish_${ID}_${SLUG}.mp4
ls -la $H/../reels/hinglish_${ID}_${SLUG}.mp4
