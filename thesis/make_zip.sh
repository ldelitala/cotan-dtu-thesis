#!/bin/bash
# Rebuild the english-only Overleaf upload zip from local sources.
set -e
cd "$(dirname "$0")"
rm -rf .overleaf
mkdir -p .overleaf
cp -r chapters images bib .overleaf/
cp main.tex .overleaf/
cd .overleaf
zip -r ../thesis_overleaf.zip . >/dev/null
cd ..
ls -lh thesis_overleaf.zip
echo "Zip ready: thesis_overleaf.zip"
