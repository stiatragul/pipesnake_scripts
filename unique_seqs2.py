import sys
import argparse
from Bio import SeqIO

def count_unique_sequences(file_paths, max_unique_sequences):
    unique_sequences_per_file = {}
    for file_path in file_paths:
        unique_sequences = set()
        for record in SeqIO.parse(file_path, "fasta"):
            sequence = str(record.seq)
            if sequence not in unique_sequences:
                unique_sequences.add(sequence)
        num_unique_sequences = len(unique_sequences)
        if num_unique_sequences <= max_unique_sequences:
            unique_sequences_per_file[file_path] = num_unique_sequences
    return unique_sequences_per_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count unique sequences in FASTA files.")
    parser.add_argument("file_paths", nargs="+", help="Path to FASTA file(s).")
    parser.add_argument("--unique", type=int, default=4,
                        help="Maximum number of unique sequences allowed. Default is 4.")
    args = parser.parse_args()
    
    file_paths = args.file_paths
    max_unique_sequences = args.unique
    
    unique_sequences_per_file = count_unique_sequences(file_paths, max_unique_sequences)
    
    for file_path, num_unique_sequences in unique_sequences_per_file.items():
        print("File:", file_path)
        print("Number of unique sequences:", num_unique_sequences)


# fasta_file = "/Users/ianbrennan/Desktop/uce-5080_identical.fasta"
# unique_count = count_unique_sequences(fasta_file)
# print(unique_count)

# I’m just going to put this here before I forget. Basically what we need to do is to read in the alignment files and identify the number of unique sequences in the file.
# Because some sequences might be unique before trimming, but identical after, we need to implement this step after trimming if the --trim parameter is used.
# Once we have the number of unique sequences in the alignment, I think we should just remove/ignore any alignments with less than 4 unique sequences. Alternatively we could just recycle the --minsamp parameter, but I think there are some reasons not to do that, though I’m not going to elaborate here.
# The basic python code for reading in the alignment and determining the number of unique sequences could be like this: