#!/bin/bash

# Build APK script for EstimatePro
echo "=========================================="
echo "Building EstimatePro APK"
echo "=========================================="

# Error handling
set -e

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null; then
    echo "Buildozer not found. Installing dependencies..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip wheel
    pip install cython buildozer
fi

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Clean previous builds if requested
if [ "$1" == "clean" ]; then
    echo "Cleaning previous builds..."
    buildozer android clean
fi

# Build the APK
echo "Starting APK build process..."
echo "This may take several minutes on first run..."
buildozer android debug

echo "=========================================="
if [ -f "bin/estimatepro-1.0.0-debug.apk" ]; then
    echo "Build successful! APK is located at:"
    echo "bin/estimatepro-1.0.0-debug.apk"
else
    echo "Build completed but APK not found. Check for errors above."
fi
echo "=========================================="