#!/bin/bash

# Define the source directory
source_dir="/home/keoghlabuser/AusARG_Proj/Sphenos/alignments/UCE"

# Define the destination directory
destination_dir="/home/keoghlabuser/AusARG_Proj/Sphenos/alignments/UCE-split"

# Number of files per subdirectory
files_per_subdir=50

# Create the destination directory if it doesn't exist
mkdir -p "$destination_dir"

# Function to copy files into subdirectories
copy_files_into_subdirs() {
    local files=("$@")
    local batch_num=1
    local batch_dir
    local remaining_files="${#files[@]}"
    
    # Loop through the files
    while [ "$remaining_files" -gt 0 ]; do
        # Create a new batch directory
        batch_dir="$destination_dir/$(basename "$source_dir")_$(printf "%02d" $batch_num)"
        mkdir -p "$batch_dir"
        
        # Determine the number of files to copy
        local files_to_copy=$((remaining_files < files_per_subdir ? remaining_files : files_per_subdir))
        
        # Copy the files into the batch directory
        for (( i = 0; i < files_to_copy; i++ )); do
            local file="${files[$((i + (batch_num - 1) * files_per_subdir))]}"
            cp "$file" "$batch_dir"
        done
        
        # Update remaining files count
        remaining_files=$((remaining_files - files_to_copy))
        
        # Increment batch number
        ((batch_num++))
    done
}

# Traverse the source directory recursively and store files in an array
all_files=()
while IFS= read -r -d '' file; do
    all_files+=("$file")
done < <(find "$source_dir" -type f -print0)

# Copy files into subdirectories
copy_files_into_subdirs "${all_files[@]}"
