# Phylogeny and Sequence Analysis

This repository contains homework assignments focused on evolutionary tree construction and sequence analysis techniques.

## Contents

### 1. Neighbor-Joining Algorithm (`NeighbourJoin.py`)
Implementation of the **Neighbor-Joining (NJ)** algorithm, a distance-based method for constructing phylogenetic trees.
- **Input**: A distance matrix of size $n \times n$.
- **Output**: An adjacency list representing the phylogeny tree with calculated limb lengths (3 decimal precision).

### 2. K-mer Based Sequence Reconstruction (`Main.java`)
A tool to determine the maximum possible occurrences of a query string within a genome reconstructed from a given set of $k$-mers.
- Calculates the upper bound of query frequency based on available $k$-mer counts.
- Handles edge cases where query length is less than $k$ (outputting -1 to indicate no bound can be determined).

### 3. Sequencing File Analysis (`Sequencing_File_Analysis.ipynb`)
Exploration of sequencing data from NCBI's Sequence Read Archive (**SRR12506197**).
- Assessment of data quality using **FastQC**.
- Understanding file formats and data extraction.

## Tools and Environment
- **Languages**: Python (NumPy), Java.
- **Tools**: FastQC, SRA Toolkit, Entrez Direct.

---
*This project was developed as part of the Bioinformatics course at Sharif University of Technology.*
