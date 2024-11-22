# practical9_ex5.py

import os
from src.clusters import readfile, scaledown, kcluster
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Path to the dataset
data_path = './datasets/zebo.txt'

# Load the dataset
row_names, col_names, data = readfile(data_path)

# Perform MDS to reduce to 2D
mds_result = scaledown(data)

# Run k-means clustering on the data in 2D space
k = 5  # Set the number of clusters
clusters = kcluster(mds_result, k=k)

# Ensure the 'img' directory exists
os.makedirs('./img', exist_ok=True)

# Plot the MDS with k-means clusters
plt.figure(figsize=(10, 8))

# Get the colormap (no need to pass k as a second argument)
colors = plt.get_cmap('tab10')

for cluster_id, cluster_points in enumerate(clusters):
    cluster_coords = np.array([mds_result[i] for i in cluster_points])
    
    # Check if the cluster is empty
    if cluster_coords.size == 0:
        continue
    
    # Check if cluster_coords is 1D (only one point in this cluster)
    if cluster_coords.ndim == 1:
        plt.scatter(cluster_coords[0], cluster_coords[1], color=colors(cluster_id), label=f'Cluster {cluster_id+1}', alpha=0.6)
    else:
        plt.scatter(cluster_coords[:, 0], cluster_coords[:, 1], color=colors(cluster_id), label=f'Cluster {cluster_id+1}', alpha=0.6)

for i, label in enumerate(row_names):
    plt.text(mds_result[i][0], mds_result[i][1], label, fontsize=8, alpha=0.75)

plt.title("MDS with K-Means Clusters")
plt.xlabel("MDS Dimension 1")
plt.ylabel("MDS Dimension 2")
plt.legend()
output_path = './img/zebo_mds_kmeans.png'
plt.savefig(output_path)
plt.show()

print(f"MDS with K-Means clustering visualization saved as {output_path}")