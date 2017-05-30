# -*- coding: UTF-8 -*-

"""
This file is part of SENSE.
(c) 2016- Alexander Loew
For COPYING and LICENSE details, please refer to the LICENSE file
"""

from distutils.core import setup # use distutils as this allows to build extensions in placee

import os
# import glob

import numpy as np
import json

# from setuptools import setup #, Extension
from setuptools import find_packages  # Always prefer setuptools over distutils
# from Cython.Distutils import build_ext
#from Cython.Build import cythonize




def xxx_get_current_version():
    ppath = os.path.dirname(os.path.realpath(__file__))
    return json.load(open(ppath + os.sep + 'geoval' + os.sep + 'version.json'))

def get_current_version():
    return '0.1'

def get_packages():
    return find_packages()


setup(name='sense',

      version=get_current_version(),

      description='xxx',

      # You can just specify the packages manually here if your project is
      # simple. Or you can use find_packages().
      # packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

      packages=get_packages(),
      #~ package_dir={'pycmbs': 'pycmbs'},
      #~ package_data={'pycmbs': ['benchmarking/configuration/*',
                               #~ 'benchmarking/logo/*', 'version.json']},

      author="Alexander Loew",
      author_email='alexander.loew@lmu.de',
      maintainer='Alexander Loew',
      maintainer_email='alexander.loew@lmu.de',

      license='APACHE 2',

      url='https://github.com/pygeo/sense',

      long_description='xxxxx',

      # List run-time dependencies here. These will be installed by pip when your
      # project is installed. For an analysis of "install_requires" vs pip's
      # requirements files see:
      # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
      # install_requires=install_requires,

      keywords=["data"],

      # To provide executable scripts, use entry points in preference to the
      # "scripts" keyword. Entry points provide cross-platform support and allow
      # pip to create the appropriate form of executable for the target
      # platform.

      #~ entry_points={
          #~ 'console_scripts': [
              #~ 'pycmbs_benchmarking = pycmbs_benchmarking:main'
          #~ ]},

      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers

    include_dirs=[np.get_include()]
      )




########################################################################
# Some useful information on shipping packages
########################################################################

# PIP


# 1) on a new computer you need to create a .pypirc file like described in the
# pypi documentation
# 2) install twine using pip install twine
# 3) generate package using: python setup.py sdist
# 4) just upload using twine upload dist/*
