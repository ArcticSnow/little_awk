'''
Set of tools and function to extract bedforms and analyze bedforms
S. Filhol, September 2022

1. study by events using start and end date
2. use the first scan as reference
3. export figures
'''


import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
import pandas as pd
import os

def plot_meteorology(ts):
    print('to be implemented')
    return

def plot_surface_change(ds, start, end, path, fname='test_*.png', figsize=(10,5), hillshade=True, dx=0.1, dy=0.1, **kwargs):
    '''
    Function to plot frames for animation
    In Progress ...

    Args:
        ds:
        start:
        end:
        path:
        fname:
        figsize:
        hillshade:
        dx:
        dy:
        **kwargs:

    Returns:

    '''
    if os.path.exists(path):
        n_digits = str(ds.time.sel(time=slice(start, end)).shape).__len__() + 1
        for i, date in enumerate(ds.time.sel(time=slice(start, end))):
            surf = ds.snow_surface.sel(time=date) - ds.snow_surface.sel(time=start)

            fig = plt.figure(figsize=figsize)
            if hillshade:
                ls = LightSource(azdeg=315, altdeg=45)
                shade = ls.hillshade(surf.values, vert_exag=0.5,
                                     dx=dx,
                                     dy=dy,
                                     fraction=1.0)


                plt.imshow(shade,
                           extent=[ds.x.min(), ds.x.max(), ds.y.min(), ds.y.max()],
                           cmap=plt.cm.gray)
            alpha=0.5
            plt.imshow(surf.values,
                           extent=[ds.x.min(), ds.x.max(), ds.y.min(), ds.y.max()],
                           cmap=plt.cm.viridis, alpha=.5, vmin=-0.1, vmax=0.5, **kwargs)
            plt.colorbar()
            plt.title(pd.to_datetime(ds.time.sel(time=date).values).strftime('%Y-%m-%d %H:%M'))
            plt.savefig(path + fname.split('*')[0] + str(i).zfill(n_digits) + fname.split('*')[1])
            plt.close()

        cmd = 'ffmpeg to be coded'
        print(f'run ffmpeg command: \n {cmd}\n')
    else:
        print(f'ERROR: path "{path}" does not exist')