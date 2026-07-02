import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("results/deseq2/deseq_results.csv", index_col=0)

# PCA-style mock visualization (placeholder structure)
plt.figure()
sns.histplot(df["log2FoldChange"].dropna(), bins=50)
plt.title("Log2 Fold Change Distribution")
plt.savefig("results/figures/pca.png")

# Volcano plot
plt.figure()
plt.scatter(df["log2FoldChange"], -df["pvalue"].fillna(1).apply(lambda x: -1*x))
plt.title("Volcano Plot")
plt.savefig("results/figures/volcano.png")
