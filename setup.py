#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='little_awk',
    version='0.0.1',
    description='A Python project to process time-lapse lidar data and extract snowpack stratigraphy',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/luc-girod/ProjectImageToDEM',

    # Author details
    author=['Simon Filhol', 'Luc Girod', 'Lucas Geffroy', 'Gaspard Boraud'],
    author_email=['simon.filhol@geo.uio.no'],

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Visualization',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords=['lidar', 'time-lapse'],
    packages=find_packages(),
    install_requires=['matplotlib',
                      'xarray',
                      'dask',
                      'datetime',
                      'pandas',
                      'numpy',
                      'gdal',
                      'pdal',
                      'scipy',
                      'geopandas',
                      'plyfile',
                      'rasterio',
                      'h5netcdf',
                      'pyyaml'],
    include_package_data=True

)
