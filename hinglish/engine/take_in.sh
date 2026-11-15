#!/bin/bash
# usage: engine/take_in.sh sNN "<signed url>"  -> archive old voice (v1_*), download new take 2, align, run test frames
set -e
ID=$1; URL=$2; H=/home/claude/tf-reels/hinglish; cd $H/work/$ID
[ -f v1_voice.mp3 ] || { mv -f voice.mp3 v1_voice.mp3; mv -f take2.mp3 v1_take2.mp3; }
curl -sS -o take2.mp3 "$URL"
cp take2.mp3 voice.mp3
python3 ../../engine/align_ctc.py voice.mp3 ../../episodes/$ID.json > align.log 2>&1
rm -rf test; python3 render.py test > test.log 2>&1
python3 ../../engine/csheet.py $ID /tmp/claude-0/-home-claude/89aeec8d-abaf-5375-8435-0af64439baf8/scratchpad/${ID}_v2 > /dev/null 2>&1 || true
tail -1 align.log
