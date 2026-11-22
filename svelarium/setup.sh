#!/usr/bin/env bash
# Prepara l'ambiente per build.py/align.py (idempotente). Uso: bash setup.sh
set -euo pipefail
cd "$(dirname "$0")"
command -v ffmpeg >/dev/null || { apt-get update -qq && apt-get install -y -qq ffmpeg; }
if [ ! -x .venv/bin/python ]; then
  python3 -m venv .venv
  .venv/bin/pip install -q "pillow>=10" "faster-whisper==1.1.0" "av<19" requests
fi
mkdir -p work
echo "setup ok"
