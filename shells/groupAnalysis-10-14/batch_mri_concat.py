'''
FileName: batch_mri_concat.py
Author: Chuncheng
Version: V0.0
Purpose: Batch script of mri_concat
'''

# %%
import os
import pandas as pd

# %%
# Where am I
# !!! If use '.' as pwd, make sure running it under the right path
pwd = '.'  # os.path.dirname(__file__)
print(f'Batch script runs at {pwd}')

# %%
# Prepare dir information
m = [
    'analysis-10',
    'analysis-11',
    'analysis-12',
    'analysis-13',
    'analysis-14',
]

d = os.path.join(pwd, 'data')

# %%
name = os.path.join(pwd, 'batch_mri_concat.sh')
with open(name, 'w') as file:
    print('#!/bin/sh', file=file)
    print('# ---------------------', file=file)
    print('# Auto generated script', file=file)
    print('# ---------------------', file=file)

    for hemi in ['lh', 'rh']:
        print(f'\n# {hemi} ---------------------', file=file)
        for niiFile in ['zstat1.nii.gz', 'zstat2.nii.gz', 'zstat3.nii.gz', 'zstat4.nii.gz', 'zstat5.nii.gz', 'zstat6.nii.gz']:
            print(f'\n# {hemi} - {niiFile} -------------------------', file=file)
            out = os.path.join(d, f'allSubjs-{niiFile}-{hemi}.mgz')
            subjs = ' '.join([os.path.join(d, f'{e}-{niiFile}-{hemi}.mgz')
                              for e in m])

            # ! Concat the subjects
            print(f'\nmri_concat {subjs} --o {out}', file=file)

            # ! Smooth the surfer
            print(
                f'\nmri_surf2surf --sval {out} --s fsaverage --hemi {hemi} --fwhm 20 --tval {out}.sm20.mgz', file=file)
    print('# ---------------------', file=file)

print(f'Generated script of {name}')

# %%
