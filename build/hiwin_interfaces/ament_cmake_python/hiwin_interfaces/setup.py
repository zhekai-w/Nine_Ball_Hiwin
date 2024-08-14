from setuptools import find_packages
from setuptools import setup

setup(
    name='hiwin_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('hiwin_interfaces', 'hiwin_interfaces.*')),
)
