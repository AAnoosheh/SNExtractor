import alipy
from astropy.io import fits

import numpy as np
import imreg_dft as ird

import os, signal
import subprocess


""" Returns FIT image in numpy array """
def readImage(filename):
  return fits.getdata(filename)

""" Writes numpy array to FIT file """
def writeImage(im, name):
    hdu = fits.PrimaryHDU()
    hdu.data = im
    hdu.writeto(name, clobber=True)

""" Returns im2 shifted and rotated relative to im1 """
def align(im1, im2, numiter, angle):
    result = ird.similarity(im1, im2, numiter=numiter, constraints={'angle': angle})
    return result['timg'], (result['tvec'][0], result['tvec'][1], result['angle'])

""" Returns blended and subtracted image """
def subtract(name1, name2, outname, offset):
    cmd = ["./hotpants", "-inim", name2, "-tmplim", name1, "-outim", outname]
    hotpants = subprocess.Popen(cmd).wait()
    try:
        os.kill(hotpants.pid, signal.SIGKILL)
    except:
        print "Process killed normally"
    return

# Currently has bug where SExtractor always gives back a 500x500 image no matter what.
# This is stopping us from using the overlapping portion of subtracted image, for now.
""" Returns list of 40x40 square images for classification """
def identify(im, threshold):
    cat = alipy.pysex.run(im, params=['X_IMAGE', 'Y_IMAGE', 'FLUX_APER'], conf_args={'PHOT_APERTURES':5})
    x, y = [], []
    for i in xrange(len(cat['X_IMAGE'])):
        if cat['FLUX_APER'][i] > threshold:
            x.append(cat['X_IMAGE'][i])
            y.append(cat['Y_IMAGE'][i])
    return np.array([x, y])