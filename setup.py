from io import open
from os.path import abspath, dirname, join
from setuptools import setup

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
    author_email='CorwinTanner@gmail.com',
    url='https://github.com/corwintanner/vmupdate',
    packages=['vmupdate'],
    entry_points={
        'console_scripts': [
            'vmupdate=vmupdate.cli:main',
        ],
    },
)
