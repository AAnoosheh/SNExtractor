import numpy as np


PATCH_SIZE = 15

def in_bounds(img, pixel):
    r,c = pixel
    half = PATCH_SIZE / 2

    if (r < half) or (r + half >= img.shape[0]):
        return False
    if (c < half) or (c + half >= img.shape[1]):
        return False
    return True

def get_patch_bounds(pixel):
    r,c = pixel
    half = PATCH_SIZE / 2

    minR, maxR = r-half, r+half+1
    minC, maxC = c-half, c+half+1
    return minR, maxR, minC, maxC


def extract_patch_around_pixel(img, pixel):
    minR, maxR, minC, maxC = get_patch_bounds(pixel)
    return img[minR:maxR, minC:maxC]

def extract_patches_outside_pixel(img, pixel):
    # http://stackoverflow.com/questions/16713991/indexes-of-fixed-size-sub-matrices-of-numpy-array
    indices = lambda x: np.arange(PATCH_SIZE, x, PATCH_SIZE)
    patches = map(lambda x : np.hsplit(x, indices(img.shape[1]))[:-1],    # Split columns
                             np.vsplit(img, indices(img.shape[0]))[:-1])  # Split rows

    # Remove patches that intersect with patch of interest
    minR, maxR, minC, maxC = [ b/PATCH_SIZE for b in get_patch_bounds(pixel) ]
    invalid_patches = set( ((minR,minC), (maxR,minC), (minR,maxC), (maxR,maxC)) )

    valid_patches = list()
    for r in xrange(len(patches)):
        for c in xrange(len(patches[0])):
            if (r,c) not in invalid_patches:
                valid_patches.append( patches[r][c] )

    return valid_patches


def rotated_patch_copies(patch):
    return np.rot90(patch, 1), \
           np.rot90(patch, 2), \
           np.rot90(patch, 3)