#!/bin/bash
# usage: engine/mux_v2.sh IDv2 outfile.mp4  (frames/ rendered; voice.mp3, sfx.wav, music.wav present) -> voice + soft SFX + music bed that ducks under the voice, loudnorm -14 LUFS
set -e
ID=$1; OUT=$2; H=/home/claude/tf-reels/hinglish; cd $H/work/$ID
ffmpeg -y -hide_banner -loglevel error -framerate 30 -i frames/f_%05d.png -i voice.mp3 -i sfx.wav -i music.wav \
 -filter_complex "[1:a]adelay=200|200,asplit=2[v][vk];[3:a]volume=0.7[m];[m][vk]sidechaincompress=threshold=0.015:ratio=3.5:attack=25:release=550:makeup=1[md];[2:a]volume=0.5[s];[v][s][md]amix=inputs=3:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=9[a]" \
 -map 0:v -map "[a]" -c:v libx264 -preset veryfast -crf 21 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart $OUT
ls -la $OUT
