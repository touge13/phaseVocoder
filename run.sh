#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <input.wav> <output.wav> <time_stretch_ratio>"
    exit 1
fi

# Assign input arguments to variables
input_file="$1"
output_file="$2"
stretch_factor="$3"

# Run the Python script
python3 src/main.py "$input_file" "$output_file" "$stretch_factor"
