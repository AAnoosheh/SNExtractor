from preprocess import *
from imgprocess import *
from classification import *


############################
KAIT_ROOT = '/media/raid0/Data/phot_processing/'  #'kait_test_images/samples/'
BAND_TYPE = ('kaitclear', 'kaitdata', 'kait*')[0]
############################


files_dict = gather_all_files(KAIT_ROOT, BAND_TYPE)
X, Y = [], []

for radec_file, matching_pairs in files_dict.iteritems():
    sn_coords = get_coords_from_file(radec_file)

    for sub_file, clear_file in matching_pairs:
        img = get_fits_data(sub_file)
        pixel = radec_to_pixel(clear_file, sn_coords)

        if not in_bounds(img, pixel):
            next

        sn_patch = extract_patch_around_pixel(img, pixel)
        sn_rot_patches = rotated_patch_copies(sn_patch)
        other_patches = extract_patches_outside_pixel(img, pixel)

        all_patches = [sn_patch] + list(sn_rot_patches) + other_patches
        X += [p.ravel() for p in all_patches]
        Y += [1]*4 + [0]*len(other_patches)


trained_model = train(X, Y)
save_model(trained_model, 'model_snapshots/SVM')