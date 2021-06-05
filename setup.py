import os
import setuptools
from distutils.core import setup

with open("README.md") as f:
    long_description = f.read()

with open(os.path.join("speechbrain", "version.txt")) as f:
    version = f.read().strip()

setup(
    name="speechbrain",
    version=version,
    description="All-in-one speech toolkit in pure Python and Pytorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mirco Ravanelli & Others",
    author_email="speechbrain@gmail.com",
    packages=setuptools.find_packages(),
    package_data={"speechbrain": ["version.txt"]},
    url="https://speechbrain.github.io/",
)
