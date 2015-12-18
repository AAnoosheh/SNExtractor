from astropy.io import fits
from astropy.coordinates import SkyCoord
from astropy import wcs

import re
from glob import glob
from collections import defaultdict


def gather_all_files(path, band):
    sub_fits =   glob(path+'*/'+band+'/*_cfsb.fit')
    clear_fits = glob(path+'*/'+band+'/*_c.fit')
    radecs =     glob(path+'*/'+band+'/rphot_radec.txt')

    clear_set, radec_set = set(clear_fits), set(radecs)
    path_dict = defaultdict(list)

    for sub in sub_fits:
        matching_clear = sub.replace('_cfsb.','_c.')
        matching_radec = sub.rpartition('/')[0] + '/rphot_radec.txt'
        if matching_clear in clear_set and matching_radec in radec_set:
            path_dict[matching_radec].append((sub, matching_clear))

    return path_dict


def get_fits_header(filename):
    hdu = fits.open(filename)[0]
    return hdu.header

def get_fits_data(filename):
    hdu = fits.open(filename)[0]
    return hdu.data


def get_coords_from_file(filename):
    for line in open(filename):
        matches = re.search(r'(\s*[+-]?\d*\.\d*)\s+([+-]?\d*\.\d*)', line)
        if matches:
            return matches.group(1,2)
    print('Error finding coordinates in radec file')

def radec_to_pixel(clear_filename, coords):
    # http://docs.astropy.org/en/stable/api/astropy.wcs.utils.skycoord_to_pixel.html#astropy.wcs.utils.skycoord_to_pixel
    s = SkyCoord(coords[0], coords[1], unit='deg')
    w = wcs.WCS(get_fits_header(clear_filename))
    xy = wcs.utils.skycoord_to_pixel(s, w)
    return xy[::-1]  #xy or yx?
