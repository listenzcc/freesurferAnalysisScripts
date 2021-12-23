'''
FileName: fetch_data.py
Author: Chuncheng
Version: V0.0
Purpose: Fetch data from the Nifiti files
'''


# %%
import os
import numpy as np
import pandas as pd
import nibabel as nib
from tqdm.auto import tqdm
from sklearn import linear_model

# %%
# ! Fetch what
pwd = os.path.dirname(__file__)


def fetch_what():
    folder = os.path.join(pwd, r'./groupAnalysis/data/')

    files = [os.path.join(folder, e)
             for e in os.listdir(folder)
             if all([
                 e.startswith('range23467subjs-'),
                 #  e.startswith('allsubjs-'),
                 e.endswith('lh.mgz'),
                 #  e.endswith('lh.mgz.sm20.mgz')
             ])]

    col_names = [os.path.basename(e).split('-', 1)[1] for e in files]

    return files, col_names


files, col_names = fetch_what()

print('There are {} files being selected, they are {}'.format(len(files), col_names))


# %%


def read_nifti(filename, verbose=True):
    img = nib.load(filename)

    # The img has the shape of (1974, 1, 83), and there are totally 163842 numbers
    # The counting is as the same as the lh-fsaverage template's 163842 vertex
    # Beware that the img is of the type of nibabel.nifti1.Nifti1Image
    if verbose:
        print('-----------------------------------------------------------')
        print(filename)
        print(type(img), img.shape, np.prod(img.shape))

    # - %%
    # The data in array format
    data = img.get_fdata()
    if verbose:
        print('-----------------------------------------------------------')
        print(data.shape, np.max(data), np.min(data))

    # - %%
    # The header, there are so many keys ...
    hdr = img.header
    if verbose:
        print('-----------------------------------------------------------')
        print('\n'.join(['| {:20s} | {} '.format(e, hdr[e]) for e in hdr]))
        print('-----------------------------------------------------------')

    return img, hdr, data

# %%


df = pd.DataFrame()

for filename, col_name in tqdm(zip(files, col_names), 'Reading files'):
    print('Working with {}'.format(col_name))

    img, hdr, data = read_nifti(filename, verbose=False)
    data = data.squeeze()
    print('Read data: {} from {}'.format(data.shape, filename))

    mean_data = np.mean(data, axis=-1)
    # mean_data = data.squeeze()[:, 0]
    print('Mean data to {}'.format(mean_data.shape))

    df[col_name] = mean_data
    pass

print(df.describe())

df.to_csv('fetched_data.csv')

# %%

# data.shape
# # %%
# y = np.ones((5, 1))
# n = len(data)
# w = -1 + np.zeros((n, ))

# for j in tqdm(range(len(data)), 'Computing GLM'):
#     regr = linear_model.LinearRegression()
#     regr.fit(y, data[j].reshape(5, 1))
#     w[j] = regr.coef_

# print(np.max(w), np.min(w))

# # %%
# y
# # %%
# data[j]

# # %%
# regr = linear_model.LinearRegression()
# regr.fit(np.array([1, 2, 3]).reshape((3, 1)),
#          np.array([1, 2, 3]).reshape((3, 1)))
# regr.coef_, regr.intercept_

# # %%
# regr = linear_model.LinearRegression()
# regr.fit(y, data[0].reshape(5, 1))
# regr.coef_, regr.intercept_

# # %%
