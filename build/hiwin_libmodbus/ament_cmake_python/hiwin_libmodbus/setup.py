from setuptools import find_packages
from setuptools import setup

setup(
    name='hiwin_libmodbus',
    version='0.0.0',
    packages=find_packages(
        include=('hiwin_libmodbus', 'hiwin_libmodbus.*')),
)
