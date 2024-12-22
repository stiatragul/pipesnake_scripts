import argparse
import glob
import os
import subprocess
import multiprocessing as mp
from tqdm import tqdm

# Lastest update 2024-12-21
# Putter

def get_args():
    parser = argparse.ArgumentParser(
        description="Infer gene trees for each loci.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "--indir",
        type=str,
        default=None,
        help="Full path to directory with the *.fasta alignments."
    )

    parser.add_argument(
        "--CPU",
        type=int,
        default=1,
        help="Number of physical CPUs to use for parallel execution."
    )

    return parser.parse_args()

def shell_iqtree(args):
    al_files = glob.glob(os.path.join(args.indir, '*.fas'))
    commands = []

    for z in al_files:
        command = f'iqtree2 -s {z} --quiet -T 1 -B 1000'
        commands.append(command)

    return commands

def run_iqtree(command):
    subprocess.call(command, shell=True)

def move_files(args):
    contree_dir = os.path.join(args.indir, 'contrees')
    iqtree_dir = os.path.join(args.indir, 'iqtree_files')

    if not os.path.exists(contree_dir):
        os.makedirs(contree_dir)
    if not os.path.exists(iqtree_dir):
        os.makedirs(iqtree_dir)

    subprocess.call(f'mv {args.indir}/*.contree {contree_dir}', shell=True)
    subprocess.call(f'mv {args.indir}/*.model.gz {iqtree_dir}', shell=True)
    subprocess.call(f'mv {args.indir}/*.log {iqtree_dir}', shell=True)
    subprocess.call(f'mv {args.indir}/*.ckp.gz {iqtree_dir}', shell=True)
    subprocess.call(f'mv {args.indir}/*.mldist {iqtree_dir}', shell=True)
    subprocess.call(f'mv {args.indir}/*.bionj {iqtree_dir}', shell=True)
    subprocess.call(f'mv {args.indir}/*.splits.nex {iqtree_dir}', shell=True)
    subprocess.call(f'mv {args.indir}/*.treefile {iqtree_dir}', shell=True)
    subprocess.call(f'mv {args.indir}/*.iqtree {iqtree_dir}', shell=True)
def main():
    args = get_args()
    commands = shell_iqtree(args)

    # Create a pool of workers for parallel execution
    pool = mp.Pool(processes=args.CPU)
    with tqdm(total=len(commands), desc="Running IQTree", unit="file") as pbar:
        for _ in pool.imap_unordered(run_iqtree, commands):
            pbar.update(1)
    pool.close()
    pool.join()

    # Move the files to appropriate directories
    move_files(args)

if __name__ == "__main__":
    main()