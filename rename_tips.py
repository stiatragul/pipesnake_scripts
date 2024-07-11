# This script is used to rename tip with a mapping file
# 2024-04-03

import sys
import csv
import os
from ete3 import Tree

def rename_tips(tree_file, mapping_file):
    # Load the tree from the tree file
    tree = Tree(tree_file)

    # Read the CSV file containing the mapping of old tip names to new tip names
    mapping = {}
    with open(mapping_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            old_name, new_name = row
            mapping[old_name.strip()] = new_name.strip()

    # Traverse the tree and replace old tip names with new tip names based on the mapping
    for leaf in tree:
        if leaf.name in mapping:
            leaf.name = mapping[leaf.name]

    # Generate output file name
    output_base = os.path.splitext(os.path.basename(tree_file))[0] + "_renamed.tre"

    # Write the modified tree to a new file
    output_file = os.path.join(os.path.dirname(tree_file), output_base)
    tree.write(outfile=output_file, format=1)

    print(f"Tree has been renamed and saved to '{output_file}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rename_tips.py <tree_file> <mapping_file>")
        sys.exit(1)

    tree_file = sys.argv[1]
    mapping_file = sys.argv[2]

    rename_tips(tree_file, mapping_file)
