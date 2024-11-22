# practical9_ex3.py

import os
from src.clusters import readfile, hcluster, drawdendrogram

# Path to the dataset
data_path = './datasets/zebo.txt'

# Load the dataset
row_names, col_names, data = readfile(data_path)

# Perform hierarchical clustering
hclust = hcluster(data)

# Ensure the 'results' and 'img' directories exist
os.makedirs('./results', exist_ok=True)
os.makedirs('./img', exist_ok=True)

# Save the dendrogram as an image
output_image_path = './img/zebo_dendrogram.jpg'
drawdendrogram(hclust, row_names, jpeg=output_image_path)

print(f"Dendrogram saved as {output_image_path}")

# Optionally, print the hierarchical structure to a text file for review
with open('./results/hclust_results.txt', 'w') as f:
    def write_clust(clust, labels=None, n=0):
        f.write(' ' * n)
        if clust.id < 0:
            f.write('-\n')
        else:
            if labels is None:
                f.write(f"{clust.id}\n")
            else:
                f.write(f"{labels[clust.id]}\n")
        if clust.left is not None:
            write_clust(clust.left, labels=labels, n=n+1)
        if clust.right is not None:
            write_clust(clust.right, labels=labels, n=n+1)

    write_clust(hclust, labels=row_names)

print("Hierarchical clustering structure saved to ./results/hclust_results.txt")