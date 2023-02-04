#!/usr/bin/env bash

# Save the path of this script's directory
script_dir=$(dirname "$0")

# Get absolute path of Python3 system interpreter
python3AbsolutePath=`which python3`

# Get absolute path of game.py
gamepyAbsolutePath="$script_dir/src/game.py"

# Start main script
bash -c "$python3AbsolutePath $gamepyAbsolutePath"

read -n 1 -s -r -p "Press any key to continue.."
