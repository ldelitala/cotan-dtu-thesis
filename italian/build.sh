#!/bin/bash
# Build thesis PDF from LaTeX source
# Usage: ./build.sh [clean]
#   - without args: incremental build (faster)
#   - with 'clean': full rebuild from scratch

set -e
cd "$(dirname "$0")"

if [ "$1" = "clean" ]; then
    echo "Cleaning build artifacts..."
    rm -rf build/*
    rm -f *.aux *.bbl *.blg *.log *.out *.synctex.gz
fi

echo "Building PDF..."
mkdir -p build
log=build/build.log
if latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error \
        -outdir=. -auxdir=./build main.tex >"$log" 2>&1; then
    echo "✅ Built: main.pdf ($(ls -lh main.pdf | awk '{print $5}'))"
else
    echo "❌ Build failed. Errors (full log: $log):"
    grep -nE ':[0-9]+:|^!' "$log" | head -30 || true
    exit 1
fi
