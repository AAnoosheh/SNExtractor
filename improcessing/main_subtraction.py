import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from pipeline_processes import *


####################### INITIALIZATION ###########################
folder = 'samples/sn2014as/'
name1 = 'NGC5410_c.fit'
name2 = '140117_NGC5410_Jan4hmpl_clear_c.fit'
verbose = True
########################## ALIGNMENT #############################
numiter = 1
angle = (0, 20) # Start at 0 degrees, +/- 20 degrees of freedom
####################### IDENTIFICATION ###########################
threshold = 2000
#################################################################


# Initialize
im1 = readImage(folder + name1)
im2 = readImage(folder + name2)

# Image Alignment with Fourier Spectrum Analysis
im2_shifted, offset = align(im1, im2, numiter, angle)

# Top Left: im1, Top Right: im2
# Bottom Left: diff(im1, im2_shifted), Bottom Right: im2_shifted
if verbose:
    ird.imshow(im1, im2, im2_shifted)
    plt.show()

# Transitory Step
name2_shifted = name2[:-4] + "_shifted.fit"
writeImage(im2_shifted, folder + name2_shifted)
outname = name1[:-4] + "_" + name2[:-4] + "_sub.fit"

# Image Subtraction with PSF
subtract(folder + name1, folder + name2_shifted, folder + outname, offset)

# Extract Points of Interest
points = identify(folder + outname, threshold)

# Plot of subtracted image with circled region for area of interest
if verbose:
    im_subtracted = readImage(folder + outname)
    plt.imshow(im_subtracted, cmap='gray', norm=LogNorm())
    plt.scatter(points[0], points[1], s=500, facecolors='none', edgecolors='r')
    plt.show()

print(points)