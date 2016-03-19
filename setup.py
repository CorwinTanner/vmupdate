from io import open
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

from vmupdate import __version__

cur_dir = abspath(dirname(__file__))

with open(join(cur_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='vmupdate',
    version=__version__,
    description="A tool to keep VM's up to date.",
    long_description=long_description,
    author='Corwin Tanner',
    author_email='corwintanner@gmail.com',
    url='https://github.com/corwintanner/vmupdate',
    packages=find_packages(),
    data_files=[
        ('config', ['vmupdate/config/vmupdate.yaml']),
        ('logging', ['vmupdate/config/logging.yaml'])],
    install_requires=['PyYAML>=3', 'keyring>=8', 'paramiko>=1'],
    entry_points={
        'console_scripts': [
            'vmupdate=vmupdate.cli:main',
        ],
    },
)
