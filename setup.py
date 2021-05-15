import os
from setuptools import setup

from rouna import version


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='rouna',
    version=version.VERSION,
    author='Alexander Pushkarev',
    author_email='alexspush@gmail.com',
    description='Minimalistic library to compare objects for equality',
    license='MIT',
    url='http://packages.python.org/rouna',
    packages=['rouna'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown'
)
