#!/bin/bash
# usage (inside day work dir): bash encode.sh OUT.mp4   (needs frames/ and mix.wav)
set -e
ffmpeg -y -loglevel error -framerate 30 -i frames/f_%05d.png -i mix.wav -vf "scale=1080:1920:flags=lanczos" -c:v libx264 -preset veryfast -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart "$1"
ffprobe -v error -show_entries format=duration,size -of default=nw=1 "$1"
