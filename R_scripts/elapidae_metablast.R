# Metablastr reciprocal blast
# Blast best reciprocal hit function to blast against target sequence FASTA. Identify best hit for each locus.

# # install BiocManager if required
# if (!requireNamespace("BiocManager", quietly = TRUE))
#   install.packages("BiocManager")
# BiocManager::install(version="3.19")
# 
# # install package dependencies
BiocManager::install(
  c(
    "Biostrings",
    "GenomicFeatures",
    "GenomicRanges",
    "Rsamtools",
    "IRanges",
    "rtracklayer",
    "Biostrings")
)


# install.packages("devtools")
# install the current version of metablastr on your system
# devtools::install_github("drostlab/metablastr", build_vignettes = TRUE, dependencies = TRUE)

library(metablastr)
# run blastn (nucleotide to nucleotide search) between example query and subject sequences

rbh_og_vit <- blast_best_reciprocal_hit(
  query = "~AusARG_Proj/Elapidae/All_Elapid_PRGs/All_loci/combined_samples_PRGs/Ogmodon_vitianus_combined.fasta",
  subject = "/home/keoghlabuser/AusARG_Proj/SqCL_Targets.fasta",
  search_type = "nucleotide_to_nucleotide",
  task = "dc-megablast",
  output.path = tempdir(),
  db.import = F
)

rbh_og_vit

rbh_lo_ela <- blast_best_reciprocal_hit(
  query = "~AusARG_Proj/Elapidae/All_Elapid_PRGs/All_loci/combined_samples_PRGs/Loveridgelaps_elapoides_combined.fasta",
  subject = "/home/keoghlabuser/AusARG_Proj/SqCL_Targets.fasta",
  search_type = "nucleotide_to_nucleotide",
  task = "dc-megablast",
  output.path = tempdir(),
  db.import = F
)

rbh_lo_ela

# exon.hits <- rbh$subject_id
# exon.hits <- sapply(exon.hits, function(x) strsplit(x, "\\|")[[1]][5])
# names(exon.hits) <- NULL
# rbh$subject_id_name <- rbh$subject_id

write.csv(rbh_og_vit, file="~AusARG_Proj/Elapidae/All_Elapid_PRGs/All_loci/combined_samples_PRGs/RBH_AllLoci_Ogmodon_vitianus.csv", row.names = F)
write.csv(rbh_lo_ela, file="~AusARG_Proj/Elapidae/All_Elapid_PRGs/All_loci/combined_samples_PRGs/RBH_AllLoci_Loveridgelaps_elapoides.csv", row.names = F)

library(Biostrings)
# Read the FASTA file

rbh_combinr <- function(.inputfasta, .rbh){
  
  fasta_file <- .inputfasta
  sequences <- readDNAStringSet(fasta_file)
  
  # Define the sample names you want to select
  selected_samples <- .rbh$query_id
  
  # Filter the sequences based on the selected sample names
  filtered_sequences <- sequences[names(sequences) %in% selected_samples]
  
  # Write the filtered sequences to a new FASTA file
  output_fasta_file <- gsub(pattern = ".fasta",x = .inputfasta, replacement = "_rbh.fasta")
  writeXStringSet(filtered_sequences, filepath = output_fasta_file, format="fasta", width = 5000)
  
}

rbh_combinr(.inputfasta = "~AusARG_Proj/Elapidae/All_Elapid_PRGs/All_loci/combined_samples_PRGs/Ogmodon_vitanus_combined.fasta", .rbh = rbh_og_vit)
rbh_combinr(.inputfasta = "~AusARG_Proj/Elapidae/All_Elapid_PRGs/All_loci/combined_samples_PRGs/Loveridgelaps_elapoides_combined.fasta", .rbh = rbh_lo_ela)

