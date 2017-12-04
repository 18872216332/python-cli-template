#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############################################
# File Name: setup.py
# Author: mafei
# Mail: fei.ma03@ele.me
# Created Time:  2017-06-26 01:25:34 AM
#############################################

from setuptools import setup, find_packages

import proxy

setup(
    name="proxy",
    version=proxy.__version__,
    description="proxy",
    long_description=open("README.rst").read(),
    license="MIT Licence",

    author="mafei",
    author_email="logan62334@gmail.com",
    url="https://github.com/logan62334/python-cli-template",

    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    platforms="any",
    install_requires=["click", "shutit"],
    entry_points={
        'console_scripts': [
            'proxy = proxy.cli:main'
        ]
    },
)
