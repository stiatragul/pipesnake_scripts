# This script is used to get tip labels from the tree files

import sys
import os
import csv
from ete3 import Tree

def extract_tip_labels(tree_file):
    # Load the tree from the Nexus file
    tree = Tree(tree_file, format=1)

    # Extract tip labels
    tip_labels = [leaf.name for leaf in tree.iter_leaves()]

    # Generate output file name
    output_file = os.path.splitext(os.path.basename(tree_file))[0] + "_tips.csv"

    # Write tip labels to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Tip Labels'])
        for label in tip_labels:
            writer.writerow([label])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_tips.py <tree_file>")
        sys.exit(1)

    tree_file = sys.argv[1]

    extract_tip_labels(tree_file)
