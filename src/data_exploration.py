#!/usr/bin/env python3

"""
A script to explore the EuroSAT dataset.

The input is the directory containing  RGB images of the EuroSAT dataset.
The sub-directories are the class names of the land cover classes.

Usage:
    To Do

Dependencies:
    To Do

Example:
    To Do

"""

import os 
from pathlib import Path
import matplotlib.pyplot as plt


# To Do
"""
- Provide an index of an image: To specify which image to select
- There are 10 classes: 
- Using matplotlib, visualise 10 sample images
- Use 2 rows and 5 cols
- Add the class name at the bottom of image
- Can save the sample image as png

"""

data_dir = './data/EuroSAT_RGB_250'
fileList = [f for f in os.listdir(data_dir) if f != '.DS_Store']

print (f"the filenames are:{fileList}")
sample_id = 10

# get the name of the images
images = [os.listdir(data_dir + '/' + f )[sample_id] for f in fileList ]
print (images)

# get the full path of the image
images_paths = [os.path.join(data_dir,i,j) for i, j in zip(fileList,images)]
print (images_paths)

# use matplotlib 
# create a grid of 5X2
# create the figure and axes grid

fig, axes = plt.subplots(nrows=2,ncols=5,figsize=(15,6))

# flatten the axes array for easy iteration

axes = axes.ravel()

# display the images in a grid

for i, img_path in enumerate(images_paths):

    file_path = Path(img_path)

    # read image using matplotlib
    img = plt.imread(img_path)

    #Display image in the corresponding subplot
    axes[i].imshow(img)

    # Remove the axes ticks and labels
    axes[i].axis("off")

    # Add titles from filenames
    axes[i].set_title(file_path.stem)
    #file_path.name gives the fname and the extension (file type)

# adjust the layout and display
plt.tight_layout

# save the plot as a jpg
# To Do

plt.show()





