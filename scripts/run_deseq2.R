library(DESeq2)
library(tidyverse)

counts <- read.csv("data/processed/count_matrix.csv", row.names=1)

# Example metadata (replace with real experiment design)
coldata <- data.frame(
  condition = c("control","control","treated","treated")
)
rownames(coldata) <- colnames(counts)

dds <- DESeqDataSetFromMatrix(
  countData = counts,
  colData = coldata,
  design = ~ condition
)

dds <- DESeq(dds)
res <- results(dds)

res <- as.data.frame(res)
write.csv(res, "results/deseq2/deseq_results.csv")
