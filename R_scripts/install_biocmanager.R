# install BiocManager if required
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install()


install.packages(c("httr", "XML", "restfulr", "curl", "devtools"))


# install package dependencies
BiocManager::install(
    c("UCSC.utils", "GenomeInfoDb", "GenomicRanges", "SummarizedExperiment", "Rhtslib", "Rsamtools", "KEGGREST", "AnnotationDbi", 
    "GenomicAlignments", "rtracklayer", "GenomicFeatures", "Biostrings"
    )
)


# install.packages("devtools")
# install the current version of metablastr on your system
devtools::install_github("drostlab/metablastr", build_vignettes = TRUE, dependencies = TRUE)