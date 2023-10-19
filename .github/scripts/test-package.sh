#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Define paths
SAMPLE_INPUT_PATH=".github/test_assets/sample_input.txt"
OUTPUT_DIRECTORY_PATH="./test_output"

# Run dirbuilder with the sample input and specified output directory
dirbuilder "$SAMPLE_INPUT_PATH" "$OUTPUT_DIRECTORY_PATH"

# Now, verify the created directory structure
if [ ! -d "$OUTPUT_DIRECTORY_PATH/root" ]; then
    echo "Directory 'root' not found!"
    exit 1
fi

if [ ! -f "$OUTPUT_DIRECTORY_PATH/root/file1.txt" ]; then
    echo "File 'file1.txt' not found in 'root' directory!"
    exit 1
fi

if [ ! -d "$OUTPUT_DIRECTORY_PATH/root/subdir" ]; then
    echo "Sub-directory 'subdir' not found in 'root' directory!"
    exit 1
fi

echo "Directory structure successfully verified!"
echo "Package seems to work as expected!"
