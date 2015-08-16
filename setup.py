#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'Cython',
    'numpy',
    'ciabatta'
]

test_requirements = [
    'Cython',
    'numpy',
    'ciabatta'
]

extensions = cythonize([
    Extension('fealty.field_numerics',
              ['fealty/field_numerics.pyx'],
              include_dirs=[numpy.get_include()]),
    Extension('fealty.walled_field_numerics',
              ['fealty/walled_field_numerics.pyx'],
              include_dirs=[numpy.get_include()]),
    Extension('fealty.lattice_numerics',
              ['fealty/lattice_numerics.pyx'],
              include_dirs=[numpy.get_include()]),
])

setup(
    name='fealty',
    version='0.1.1',
    description='Discretised field utilities',
    long_description=readme + '\n\n' + history,
    author='Elliot Marsden',
    author_email='elliot.marsden@gmail.com',
    url='https://github.com/eddiejessup/fealty',
    packages=setuptools.find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    install_requires=requirements,
    license='BSD',
    zip_safe=False,
    keywords='fealty',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    ext_modules=extensions,
)
