# Use this script to rename raw reads files downloaded from BioPlatforms.
# This one particularly for Eugongylinae files.
# Problem is there a -ACTACA tag after so want to get rid of this 

import os
import sys
import re

def remove_pattern_from_filenames(directory, pattern):
    # Compile the regex pattern
    regex_pattern = re.compile(pattern)

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        # Check if the filename matches the pattern
        if regex_pattern.search(filename):
            # Replace the pattern with an empty string
            new_filename = regex_pattern.sub('', filename)
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f'Renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory> <pattern>")
        sys.exit(1)

    # Get directory path and pattern from command-line arguments
    directory = sys.argv[1]
    pattern = sys.argv[2]

    # Call the function to remove the pattern from filenames
    remove_pattern_from_filenames(directory, pattern)
