#!/usr/bin/env bash

# Save the path of this script's directory
script_dir=$(dirname "$0")

# Get absolute path of Python3 system interpreter
python3AbsolutePath=`which python3`

# Get absolute path of game.py
gamepyAbsolutePath="$script_dir/src/game.py"

# If parameter is not empty
if [[ -n "$1" ]]; then
    bash -c "$python3AbsolutePath $gamepyAbsolutePath $1"
else
    # No parameter detected, proceed normal console execution
    bash -c "$python3AbsolutePath $gamepyAbsolutePath"
fi
echo " "
read -n 1 -s -r -p "Press any key to continue.."
echo " "


