#!/bin/bash

# Build APK script for EstimatePro
echo "=========================================="
echo "Building EstimatePro APK"
echo "=========================================="

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null; then
    echo "Buildozer not found. Installing dependencies..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install cython buildozer
fi

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Clean previous builds (optional - uncomment if needed)
# buildozer android clean

# Build the APK
echo "Starting APK build process..."
buildozer android debug

echo "=========================================="
echo "Build complete! Check bin/ directory for APK"
echo "=========================================="

