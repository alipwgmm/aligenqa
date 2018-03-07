from setuptools import setup
from glob import glob

install_requires = ['rootpy', 'argparse']

setup(
    name='aligenqa',
    version='0.0.2',
    description="Provides tools for post-processing of MC multiplicity estimator studies",
    author='Christian Bourjau',
    author_email='christian.bourjau@cern.ch',
    packages=['aligenqa', 'roofie'],
    long_description=open('README.md').read(),
    scripts=glob('scripts/*'),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
   install_requires=install_requires,
)
