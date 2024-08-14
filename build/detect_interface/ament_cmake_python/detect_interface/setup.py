from setuptools import find_packages
from setuptools import setup

setup(
    name='detect_interface',
    version='0.0.0',
    packages=find_packages(
        include=('detect_interface', 'detect_interface.*')),
)
