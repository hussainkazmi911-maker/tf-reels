#!/bin/bash
# usage: engine/queue.sh "s03:rep_dms s04:cart ..."  -> renders sequentially; waits for work/sNN/READY for each
H=/home/claude/tf-reels/hinglish
for pair in $1; do
  ID=${pair%%:*}; SLUG=${pair##*:}
  while [ ! -f $H/work/$ID/READY ]; do sleep 5; done
  cd $H/work/$ID && rm -rf frames DONE
  python3 ../../engine/dump_sfx.py > sfx.log 2>&1
  (python3 render.py run 2 0 > r0.log 2>&1 & python3 render.py run 2 1 > r1.log 2>&1 & wait)
  bash ../../engine/mux_story.sh $ID $SLUG > mux.log 2>&1 && rm -rf frames && echo done > DONE
  echo "$ID finished $(date +%T)" >> $H/work/queue.log
done
