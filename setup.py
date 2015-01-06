from setuptools import setup, find_packages
import sys
import os
from glob import glob
import platform

if os.name == 'nt':
    pgm_files = os.environ["ProgramFiles"]
    base_files = os.path.join(pgm_files, 'diamond')

if os.name == 'nt':
    pkgPath(os.path.join(base_files, 'collectors'), 'src/collectors', '\\')
else:
    pkgPath('share/diamond/collectors', 'src/collectors')

setup(
    name = "diamond-solariskstat",
    version = "0.1",
    package_dir = {'': 'src'},
    packages = find_packages(),
    author = "Puppet Labs",
    description = "Collection of diamond collectors that extract data from Solaris kstats.",
    license = "ALv2",
    keywords = "diamond solaris kstats kstat zfs",
    url = "http://github.com/puppetlabs/diamond-solariskstat",
    install_requires = ['diamond'],
)
