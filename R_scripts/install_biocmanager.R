# install BiocManager if required
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install()

### If installing on linux you might have to install other dependencies outside first
install.packages(c("ragg", "pkgdown", "httr", "XML", "restfulr", "curl", "devtools"))

.libPaths("~/R/x86_64-pc-linux-gnu-library/4.4")
.libPaths()


# install package dependencies
BiocManager::install(
    c("UCSC.utils", "GenomeInfoDb", "GenomicRanges", "SummarizedExperiment", "Rhtslib", "Rsamtools", "KEGGREST", "AnnotationDbi", 
    "GenomicAlignments", "rtracklayer", "GenomicFeatures", "Biostrings"
    ), lib = "~/R/x86_64-pc-linux-gnu-library/4.4"
)

library(devtools)

# install.packages("devtools")
# install the current version of metablastr on your system
devtools::install_github("drostlab/metablastr", build_vignettes = TRUE, dependencies = TRUE)
