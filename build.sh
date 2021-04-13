#!/bin/bash
# Build the virtual environment

# Where the virtual environment is built
builddir=$(dirname $0)

# Make directory for virtual environment if it does not exist
if test ! -d $builddir/venv; then
    mkdir $builddir/venv
fi

# Check if the virtual environment is already built
if ls -1qA $builddir/venv | grep -q .; then
    echo "Directory $builddir/venv is not empty ... please start with an empty virtual environment directory ... exiting"
    exit
fi

# The path to the desired python to use
python=/usr/bin/python3

# Make the virtual environment
virtualenv --python=$python $builddir/venv

# Source the virtual environment to activate it
source $builddir/venv/bin/activate

# Install pip packages using pip
pip3 install -r $builddir/requirements.txt

# Get versions of the installed pip packages for freezing the version numbers
echo "Frozen pip package version numbers:"
python -m pip freeze | tee $builddir/requirements_frozen.txt
