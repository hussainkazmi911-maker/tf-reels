#!/bin/bash
# One-time setup of the shared work folder /home/claude/forge (safe to re-run).
set -e
F=/home/claude/forge; REPO=$(cd "$(dirname "$0")/.." && pwd)
mkdir -p $F && cd $F
pip install --break-system-packages -q kokoro-onnx soundfile numpy pillow 2>&1 | tail -1 || true
[ -d node_modules/@fontsource/inter ] || npm i --silent @fontsource/inter
[ -f kokoro.onnx ] || curl -sSL -o kokoro.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
[ -f voices.bin ]  || curl -sSL -o voices.bin  https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
cp $REPO/pipeline/logo.png $REPO/pipeline/base.css .
ls -la $F | head -12
