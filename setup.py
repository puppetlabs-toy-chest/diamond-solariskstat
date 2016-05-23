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
    data_files.append((os.path.join(base_files, 'collectors/solariskstat'), glob('src/collectors/solariskstat/*')))
    data_files.append((os.path.join(base_files, 'collectors/solariskstat'), []))
else:
    data_files.append(('share/diamond/collectors/solariskstat/', glob('src/collectors/solariskstat/*')))
    data_files.append(('share/diamond/collectors/solariskstat', []))

setup(
    name = "diamond-solariskstat",
    version = "0.2",
    package_dir = {'': 'src'},
    packages = find_packages(),
    data_files = data_files,
    author = "Puppet Labs",
    author_email = "info@puppetlabs.com",
    description = "Collection of diamond collectors that extract data from Solaris kstats.",
    license = "ALv2",
    keywords = "diamond solaris kstats kstat zfs",
    url = "http://github.com/puppetlabs/diamond-solariskstat",
    install_requires = ['diamond'],
    zip_safe = 0
)
