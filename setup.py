from setuptools import setup, find_packages
import sys
import os
from glob import glob
import platform

data_files = []

if os.name == 'nt':
    pgm_files = os.environ["ProgramFiles"]
    base_files = os.path.join(pgm_files, 'diamond')

def pkgPath(root, path, rpath="/"):
    """
        Package up a path recursively
    """
    global data_files
    if not os.path.exists(path):
        return
    files = []
    for spath in os.listdir(path):
        # Ignore test directories
        if spath == 'test':
            continue
        subpath = os.path.join(path, spath)
        spath = os.path.join(rpath, spath)
        if os.path.isfile(subpath):
            files.append(subpath)
        if os.path.isdir(subpath):
            pkgPath(root, subpath, spath)
    data_files.append((root + rpath, files))

if os.name == 'nt':
    pkgPath(os.path.join(base_files, 'collectors/solariskstat'), 'src/collectors/solariskstat', '\\')
else:
    pkgPath('share/diamond/collectors/solariskstat', 'src/collectors/solariskstat')

setup(
    name = "diamond-solariskstat",
    version = "0.1",
    package_dir = {'': 'src'},
    packages = find_packages(),
    author = "Puppet Labs",
    author_email = "info@puppetlabs.com",
    description = "Collection of diamond collectors that extract data from Solaris kstats.",
    license = "ALv2",
    keywords = "diamond solaris kstats kstat zfs",
    url = "http://github.com/puppetlabs/diamond-solariskstat",
    data_files=data_files,
    install_requires = ['diamond']
)
