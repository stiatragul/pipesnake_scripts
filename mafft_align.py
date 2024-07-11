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

def align_fasta(fasta_file):
    output_file = os.path.splitext(fasta_file)[0] + ".aln"
    subprocess.run(['mafft', '--maxiterate', '1000', '--globalpair', '--adjustdirection', '--quiet', fasta_file], stdout=open(output_file, 'w'), check=True)
    return fasta_file

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Align FASTA files in parallel.')
    parser.add_argument('directory', type=str, help='Directory containing FASTA files')
    parser.add_argument('cpu', type=int, help='Number of CPU cores to use for parallel processing')
    args = parser.parse_args()

    # List all FASTA files in the specified directory
    fasta_files = [os.path.join(args.directory, filename) for filename in os.listdir(args.directory) if filename.endswith('.fasta')]

    # Align each FASTA file in parallel with a progress bar
    with ThreadPoolExecutor(max_workers=args.cpu) as executor, tqdm(total=len(fasta_files), desc='Aligning FASTA files') as pbar:
        futures = [executor.submit(align_fasta, fasta_file) for fasta_file in fasta_files]
        for future in futures:
            future.result()  # Wait for each alignment to finish
            pbar.update(1)   # Update progress bar
