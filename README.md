# Adhoc pipesnake scripts

Scripts in this directory are a combination of early versions of scripts that became the `pipesnake` pipeline and additional scripts that I wrote to help with managing and assessing data associated with the `pipesnake` workflow.

These scripts are often designed to be more flexible and general, and ARE NOT identical to scripts of the same name housed in ~/.nextflow/assets/ausarg/pipesnake/bin

Be careful when using these. Here are some sample commands:

python3 pipesnake_scripts/phylogeney_make_alignments_old.py --file Diplodactylidae/PRG/lineage.csv --dir Diplodactylidae/PRG 
This pulled together what we were calling "rough" or "raw" alignments


### Early pipesnake scripts (by Ian Brennan)
- `BPA_process_metadata.py`
- `unique_seqs2.py`
- `Count_barcode_frequency.py` - Used for counting barcode frequencies in fastq.gz raw reads files. 
- `phylogeny_align_genetrees_old.py`
- `phylogeny_make_alignments_old.py`


### Other code that are helpful
- `PRG_subset.py` - subset loci from PRG files depending on prefix (e.g. ">AHE" or ">UCE").
- `PRG_loci_stats.py` - This is use to get the number of AHE, UCE, or gene of each fasta file (PRGs) in a directory.
- `PRG_samp_rename.py` - script looks at each fasta file and see that it doesn't start with >AHE or >uce, then make it start with >gene. This is just for consistency.
- `check_lineage_sampleinfo.py` - Used for finding duplicates or weird characters including: (); spaces; /; \; in lineage row that will cause issues in the pipeline. 
- `check_unique.py`
- `rename_tips.py` - This is use for renaming tips according to a csv. We can use this to rename the .tree file or the contree files.
- `mafft_align.py` - This this script to align files when we have fasta files that have Rabosky data appended to AusARG data. This happens when gene file names are not the same in the original pipeline. So have to manually append different versions.
- `iqtree_log_parse.py` - Used for parsing information from .log files from IQTREE analyses.
- `phylogeny_genetrees_gen*.py`- variations of ways to run iqtree analyses in a dir full of alignments
- `segul_topo_test.py` - combine SEGUL summary and pick out the alignments that have max. ntaxa and minimum missing data. It then concatenates those files and this can be used for topology test. 
- `raw_reads_rename.py` - Use this script to rename raw reads files downloaded from BioPlatforms.
- `tip_labels_2_csv.py` - outputs tip labels from the tree files to a csv.

### Bash scripts
- `split_files.sh` - split alignment files into multiple directories (useful for running phylogeny_genetree_gen*.py on different machines).

### Julia script
- `correction_multi_aggressive.jl` - script from Janne Torkkola to trim alignments using TAPER.