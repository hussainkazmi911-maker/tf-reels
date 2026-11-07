#!/bin/bash
# usage: bash pipeline/newday.sh NN   -> creates /home/claude/forge/dayNN from days/dayNN (sources) with links to shared files
set -e
NN=$1; F=/home/claude/forge; REPO=$(cd "$(dirname "$0")/.." && pwd); W=$F/day$NN
mkdir -p $W && cd $W
for f in kokoro.onnx voices.bin node_modules logo.png; do ln -sf $F/$f $f; done
cp $REPO/pipeline/{tts.py,mkcfg.py,render.py,sheet.py,encode.sh} .
cp $REPO/days/day$NN/{script.json,build.py,reel.js,mkaudio.py} .
echo "work dir: $W"
