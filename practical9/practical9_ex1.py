from src.clusters import readfile, hcluster, drawdendrogram

# Load the data from blogdata.txt
rownames, colnames, data = readfile('./datasets/blogdata.txt')

# Perform hierarchical clustering
blog_clusters = hcluster(data)

# Draw the dendrogram and save it as a JPEG image
drawdendrogram(blog_clusters, rownames, jpeg='./img/blog_dendrogram.jpg')

print("Exercise 1 completed. Dendrogram saved as 'blog_dendrogram.jpg'.")