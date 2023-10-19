#!/bin/bash

# This script is used to verify if the generated directory structure matches the expected structure.
# It should be placed in .github/test_assets/ and run after executing the dirbuilder tool.

BASE_DIR="$1"

# Check root directory
if [ ! -d "${BASE_DIR}/root" ]; then
    echo "Directory 'root' not found!"
    exit 1
fi

# Check file in the root directory
if [ ! -f "${BASE_DIR}/root/file1.txt" ]; then
    echo "File 'file1.txt' not found in 'root' directory!"
    exit 1
fi

# Check sub-directory in root
if [ ! -d "${BASE_DIR}/root/subdir" ]; then
    echo "Sub-directory 'subdir' not found in 'root' directory!"
    exit 1
fi

echo "All checks passed!"
exit 0
