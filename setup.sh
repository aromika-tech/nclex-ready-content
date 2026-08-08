#!/usr/bin/env bash
# One-off setup on a fresh machine. Safe to re-run.
set -e
python3 -m pip install --quiet --break-system-packages playwright pillow qrcode || \
python3 -m pip install --quiet playwright pillow qrcode
# Chromium is preinstalled in the Cowork cloud container. Elsewhere, fetch it once.
python3 -c "import pathlib,os;p=os.environ.get('PLAYWRIGHT_BROWSERS_PATH','');\
import sys;sys.exit(0 if p and pathlib.Path(p).exists() else 1)" \
  || python3 -m playwright install chromium
echo "ready. try: cd content && python3 today.py"
