#!/bin/bash
# Run the python script inside the virtual environment

# Set up directories
dir=$(dirname $0)
venvdir=$(dirname $0)/venv

# Activate the virtual environment
if test -e $venvdir/bin/activate; then
    source $venvdir/bin/activate
else
    echo "Error: virutual environment not found (maybe it was not built)  ... exiting"
    exit 1
fi

# Python runs inside the virtual environment from here on:
python $dir/example.py



