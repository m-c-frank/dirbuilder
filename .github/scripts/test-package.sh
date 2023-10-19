#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Your bash commands to test the package
# For example:
# dirbuilder [input_file_path] [output_directory_path]

# If dirbuilder is a command-line utility after installing the package
dirbuilder --version

# Or if you want to run python and then test:
# python -c 'import dirbuilder; print(dirbuilder.__version__)'

echo "Package seems to work as expected!"
