# script looks at each fasta file and see that it doesn't start with >AHE or >uce, then make it start with >gene
import os
import sys

# Function to append ">gene-" to lines starting with ">" but not ">AHE" or ">UCE"
def append_gene_prefix(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('>') and not line.startswith('>AHE') and not line.startswith('>uce'):
                outfile.write('>gene-' + line[1:])
            else:
                outfile.write(line)

# Get input and output file paths from command-line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <input_dir> <output_dir>")
    sys.exit(1)

input_dir = sys.argv[1]
output_dir = sys.argv[2]

# Process each .fasta file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".fasta"):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename)
        append_gene_prefix(input_file, output_file)

print("Files processed successfully.")
