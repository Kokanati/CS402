#!/bin/bash

# Input file
input_file="270824passwords.txt"

# Output file
output_file="passwords.txt"

# Clear the output file if it exists
> "$output_file"

# Read the input file line by line
while IFS= read -r line; do
  # Check if the line has exactly 20 characters
  if [ ${#line} -eq 20 ]; then
    # Write the line to the output file
    echo "$line" >> "$output_file"
  fi
done < "$input_file"

echo "Script execution completed. Check '$output_file' for results."

