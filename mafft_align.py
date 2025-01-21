# This this script to align files when we have fasta files that have Rabosky data appended to AusARG data. This happens when gene file names are not the same
# in the original pipeline. So have to manually append different versions 

# gene1_AHR.fasta
# gene2_AHR.fasta
# gene1_BDNF.fasta
# gene2_BDNF.fasta
# in to gene-AHR.fasta and gene-BDNF.fasta These need to be re-aligned.

import os
import subprocess
import argparse
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def align_fasta(fasta_file, output_extension):
    """
    Aligns a FASTA file using MAFFT and saves the aligned output.

    Parameters:
        fasta_file (str): Path to the input FASTA file.
        output_extension (str): Desired file extension for the output file.
    """
    output_file = os.path.splitext(fasta_file)[0] + output_extension
    subprocess.run(
        ['mafft', '--maxiterate', '1000', '--globalpair', '--adjustdirection', '--quiet', fasta_file],
        stdout=open(output_file, 'w'),
        check=True
    )
    return fasta_file

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Align FASTA files in parallel using MAFFT.')
    parser.add_argument('-d', '--directory', required=True, type=str, help='Directory containing FASTA files')
    parser.add_argument('--cpu', type=int, default=1, help='Number of CPU cores to use for parallel processing (default: 1)')
    parser.add_argument('--output-format', type=str, default='.aln', help='Output file extension (default: .aln)')
    args = parser.parse_args()

    # Validate output extension
    if not args.output_format.startswith('.'):
        args.output_format = '.' + args.output_format

    # List all FASTA files in the specified directory
    fasta_files = [os.path.join(args.directory, filename) for filename in os.listdir(args.directory) if filename.endswith('.fasta')]

    if not fasta_files:
        print(f"No FASTA files found in the directory: {args.directory}")
        exit(1)

    # Align each FASTA file in parallel with a progress bar
    with ThreadPoolExecutor(max_workers=args.cpu) as executor, tqdm(total=len(fasta_files), desc='Aligning FASTA files') as pbar:
        futures = [executor.submit(align_fasta, fasta_file, args.output_format) for fasta_file in fasta_files]
        for future in futures:
            future.result()  # Wait for each alignment to finish
            pbar.update(1)   # Update progress bar

    print("All FASTA files have been successfully aligned!")
