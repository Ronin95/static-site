#!/bin/bash
# 1. Run the Python generation script
python3 src/main.py

# 2. Change into the public directory and start the server
cd public && python3 -m http.server 8888