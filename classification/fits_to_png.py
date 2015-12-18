from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import sys
import glob


def show_dir(dirname):
    for filename in glob.glob(dirname + '*.fit'):
        show_image(filename, save=True)

def show_image(filename, save=False):
    img = get_img_data(filename)
    try:
        plt.imshow(img, cmap='gray', norm=LogNorm())
        plt.colorbar()

        if save:
            plt.savefig(filename.split('.')[0] + '.png', \
                        bbox_inches='tight')
        else:
            plt.show()
        plt.close()

    except TypeError:
        print("Invalid fits file: "+filename)

def get_img_data(filename):
    hdu = fits.open(filename)[0]
    return hdu.data



arg = sys.argv[1]

if '.' in arg:
    show_image(arg)
else:
    if not arg.endswith('/'):  arg += '/'
    show_dir(arg)
