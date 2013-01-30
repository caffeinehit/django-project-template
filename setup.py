#!/usr/bin/env python

from setuptools import setup, find_packages
import {{ project_name }}

setup(
    name='{{ project_name }}',
    version={{ project_name }}.__version__,
    description='',
    url='',
    author='',
    author_email='',
    packages=find_packages(),
    include_package_data=True,
    install_requires = [],
)
