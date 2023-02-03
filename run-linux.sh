#!/usr/bin/env bash

# Get absolute path of Python3 system interpreter
python3AbsolutePath=`which python3`

# Start main script
bash -c "$python3AbsolutePath ./src/game.py"

