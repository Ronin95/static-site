#!/bin/bash
echo "Building production site..."

# Pass the basepath (your repo name) as an argument to main.py
# Make sure to include the slashes!
python3 src/main.py "/static-site/"

echo "Build complete. Commit the 'docs' directory and push to GitHub."