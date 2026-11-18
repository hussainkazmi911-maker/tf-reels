#!/bin/bash
# usage: engine/queue_v2.sh "s07v2:hinglish_s07_brand_takeover_v2 s02v2:hinglish_s02_cod_returns_v2"
H=/home/claude/tf-reels/hinglish
for pair in $1; do
  ID=${pair%%:*}; OUT=${pair##*:}
  cd $H/work/$ID && rm -rf frames DONE
  python3 ../../engine/dump_sfx2.py > sfx.log 2>&1
  (python3 render.py run 2 0 > r0.log 2>&1 & python3 render.py run 2 1 > r1.log 2>&1 & wait)
  bash ../../engine/mux_v2.sh $ID /home/claude/tf-reels/reels/$OUT.mp4 > mux.log 2>&1 && echo done > DONE
  echo "$ID finished $(date +%T)" >> $H/work/queue_v2.log
done
