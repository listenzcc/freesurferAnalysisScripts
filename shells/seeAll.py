# %%
import os
import numpy as np
import nibabel as nib


# %%

def read_nifti(filename):
    img = nib.load(filename)

    # The img has the shape of (1974, 1, 83), and there are totally 163842 numbers
    # The counting is as the same as the lh-fsaverage template's 163842 vertex
    # Beware that the img is of the type of nibabel.nifti1.Nifti1Image
    print('-----------------------------------------------------------')
    print(filename)
    print(type(img), img.shape, np.prod(img.shape))

    # - %%
    # The data in array format
    data = img.get_fdata()
    print('-----------------------------------------------------------')
    print(data.shape, np.max(data), np.min(data))

    # - %%
    # The header, there are so many keys ...
    hdr = img.header
    print('-----------------------------------------------------------')
    print('\n'.join(['| {:20s} | {} '.format(e, hdr[e]) for e in hdr]))
    print('-----------------------------------------------------------')

    return img, hdr, data

# %%


pwd = os.path.dirname(__file__)

for stat in ['zstat1.nii.gz', 'zstat2.nii.gz', 'zstat3.nii.gz', 'zstat4.nii.gz', 'zstat5.nii.gz', 'zstat6.nii.gz']:
    filename = os.path.join(
        pwd, r'groupAnalysis/data/allsubjs-{}-lh.mgz'.format(stat))

    assert os.path.isfile(filename), f'File not Found:{filename}'

    img, hdr, data = read_nifti(filename)

# %%
meandata = np.mean(data, axis=-1, keepdims=True)
print(meandata.shape)
hdr['dims'] = meandata.shape
img = nib.freesurfer.mghformat.MGHImage(
    meandata.reshape((163842, 1, 1)), affine=img.affine, header=hdr, file_map=img.file_map)
nib.save(img, os.path.join(pwd, 'example.mgz'))

# %%
np.max(meandata), np.min(meandata)
# %%
