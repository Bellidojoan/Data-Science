# practical9_ex4.py

import os
from src.clusters import readfile, scaledown, draw2d

# Path to the dataset
data_path = './datasets/zebo.txt'

# Load the dataset
row_names, col_names, data = readfile(data_path)

# Perform multidimensional scaling (MDS)
mds_result = scaledown(data)

# Ensure the 'img' directory exists
os.makedirs('./img', exist_ok=True)

# Save the 2D plot of the MDS result
output_image_path = './img/zebo_mds.jpg'
draw2d(mds_result, row_names, jpeg=output_image_path)

print(f"MDS visualization saved as {output_image_path}")