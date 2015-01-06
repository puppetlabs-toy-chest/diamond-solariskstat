from setuptools import setup, find_packages
import sys
import os
from glob import glob
import platform

data_files = []

if os.name == 'nt':
    pgm_files = os.environ["ProgramFiles"]
    base_files = os.path.join(pgm_files, 'diamond')

if os.name == 'nt':
    data_files.append((os.path.join(base_files, 'collectors/solariskstat'), ['src/collectors/solariskstat/solarisfs.py', 'src/collectors/solariskstat/solarisarc.py']))
else:
    data_files.append(('share/diamond/collectors/solariskstat', ['src/collectors/solariskstat/solarisfs.py', 'src/collectors/solariskstat/solarisarc.py']))

setup(
    name = "diamond-solariskstat",
    version = "0.1",
    package_dir = {'': 'src'},
    data_files = data_files,
    packages = find_packages(),
    author = "Puppet Labs",
    author_email = "info@puppetlabs.com",
    description = "Collection of diamond collectors that extract data from Solaris kstats.",
    license = "ALv2",
    keywords = "diamond solaris kstats kstat zfs",
    url = "http://github.com/puppetlabs/diamond-solariskstat",
    install_requires = ['diamond'],
    zip_safe = 0
)
