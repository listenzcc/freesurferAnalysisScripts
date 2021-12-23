'''
FileName: batch_mris_preproc.py
Author: Chuncheng
Version: V0.0
Purpose: Batch script for group analysis
'''

# %%
import os
import sys
import pandas as pd

# %%
# Where am I
# !!! If use '.' as pwd, make sure running it under the right path
pwd = '.'  # os.path.dirname(__file__)
print(f'Batch script runs at {pwd}')

# %%
# Prepare dir information
m = [
    ('analysis-10', 'liuyeSubject10'),
    ('analysis-11', 'liuyeSubject11'),
    ('analysis-12', 'liuyeSubject12'),
    ('analysis-13', 'liuyeSubject13'),
    ('analysis-14', 'liuyeSubject14'),
]

d = os.path.join(pwd, '..', 'featdirs')

df = pd.DataFrame(m, columns=['featName', 'subjectName'])
df['featPath'] = df['featName'].map(lambda e: os.path.join(d, e))

df

# %%
# ! It should equal to the number of featDirs
df['featPathSubCount'] = df['featPath'].map(lambda e: len(os.listdir(e)))

# %%
d = os.path.join(pwd, 'data')
if not os.path.isdir(d):
    os.mkdir(d)


def mris_preproc(featName, featPath, niiFile, hemi):
    '''Generate mris_preproc command by featName'''
    target = 'fsaverage'
    out = os.path.join(d, f'{featName}-{niiFile}-{hemi}.mgz')
    feats = [os.path.join(featPath, e) for e in os.listdir(featPath)]

    runs = ' '.join(
        f'--iv {e}/stats/{niiFile} {e}/reg/freesurfer/anat2exf.register.dat' for e in feats)

    return f'mris_preproc --out {out} --target {target} --hemi {hemi} --mean {runs}'


name = os.path.join(pwd, 'batch_mris_preproc.sh')
with open(name, 'w') as file:
    print('#!/bin/sh', file=file)
    print('# ---------------------', file=file)
    print('# Auto generated script', file=file)
    print('# ---------------------', file=file)
    for hemi in ['lh', 'rh']:
        print(f'# {hemi} ---------------------', file=file)
        for niiFile in ['zstat1.nii.gz', 'zstat2.nii.gz', 'zstat3.nii.gz', 'zstat4.nii.gz', 'zstat5.nii.gz', 'zstat6.nii.gz']:
            print(f'# {hemi} - {niiFile} -------------------------', file=file)
            print('\n'.join([mris_preproc(n, p, niiFile, hemi)
                            for n, p in zip(df['featName'], df['featPath'])]),
                  file=file)
    print('# ---------------------', file=file)

print(f'Generated script of {name}')

# %%
