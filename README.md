# RNA-seq Differential Expression Analysis Pipeline

This project implements a reproducible RNA-seq differential expression analysis workflow using Snakemake, R (DESeq2), and Python. The pipeline follows a standard computational biology workflow used in transcriptomics studies in biomedical research and drug discovery.

---

## Objective

To identify differentially expressed genes between experimental conditions using RNA-seq count data and provide a reproducible, modular analysis workflow suitable for biomedical and translational research.

---

## Workflow Overview

Quality Control → Count Processing → Differential Expression → Visualization → Biological Interpretation

---

## Technologies

- Python (pandas, numpy, matplotlib, seaborn)
- R (DESeq2, ggplot2, tidyverse)
- Snakemake (workflow management)
- Jupyter Notebook (exploratory analysis)

---

## Outputs

- Normalized gene expression matrix
- Differential expression results (log2 fold change, adjusted p-values)
- PCA plots of sample structure
- Volcano plots of gene significance
- Heatmaps of top differentially expressed genes

---

## Project Structure

See `/workflow`, `/scripts`, and `/results` for pipeline components and outputs.

---

## Reproducibility

To recreate the environment:

```bash
conda env create -f environment.yml
conda activate rna-seq
