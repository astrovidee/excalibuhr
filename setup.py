# File: setup.py
from setuptools import find_packages, setup

setup(
    name="excalibuhr",
    version="0.1.1",
    license='MIT',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    author='Yapeng Zhang',
    author_email='yapzhang@caltech.edu',
    url='https://github.com/yapenzhang/excalibuhr',
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'astropy',
        'matplotlib',
        'astroquery',
        'skycalc_ipy',
    ],
)
