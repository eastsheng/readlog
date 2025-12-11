"""run this
python setup.py sdist
pip install .
"""

# from distutils.core import setup
from setuptools import setup, find_packages
import json

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt","r") as f:
    required = f.read().splitlines()

with open('./src/__init__.py', 'r', encoding='utf-8') as f:
    data = json.load(f)
version = data["version"]

setup(
name         = 'readlog',
version      = version,
py_modules   = ['readlog'],
author       = 'CHENDONGSHENG',
author_email = 'eastsheng@hotmail.com',
packages=find_packages('src'),
package_dir={'': 'src'},
install_requires=required,
url          = 'https://github.com/eastsheng/readlog',
description  = 'Read themo info from lammps output file or log file',
long_description=long_description,
long_description_content_type='text/markdown'
)

