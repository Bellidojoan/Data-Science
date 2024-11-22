# practical9_ex2.py

# Import the necessary modules and functions
import os
from src.clusters import readfile, kcluster

# Load the data
rownames, colnames, data = readfile('./datasets/blogdata.txt')

# Set the number of clusters
num_clusters = 5

# Perform k-means clustering
clusters = kcluster(data, k=num_clusters)

# Display results
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}:")
    for row_id in cluster:
        print(f" - {rownames[row_id]}")
    print("\n")

# Ensure the 'results' directory exists
os.makedirs('./results', exist_ok=True)

# Save the output in a file
with open('./results/kcluster_results.txt', 'w') as f:
    for i, cluster in enumerate(clusters):
        f.write(f"Cluster {i + 1}:\n")
        for row_id in cluster:
            f.write(f" - {rownames[row_id]}\n")
        f.write("\n")