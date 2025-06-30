#!/bin/bash
# Simple helper script to run the leadbot using the virtual environment if
# available.
DIR="$(cd "$(dirname "$0")" && pwd)"
if [ -d "$DIR/venv" ]; then
    source "$DIR/venv/bin/activate"
fi
python "$DIR/autopilot_leadbot.py"
