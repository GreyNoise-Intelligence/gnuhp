#!/usr/bin/env python
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='uhp',
    version='1.1.1',
    description='Universal Honeypot.',
    url="https://github.com/MattCarothers/uhp",
    author="Matt Carothers",
    author_email="test@example.com",
    maintainer = "Matt Carothers",
    maintainer_email = "test@example.comm",
    license="BSD",
    packages=find_packages(),
    install_requires=[],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: Unlicensed',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries'
    ],
    package_data={
        'uhp': [],
    },
    entry_points={
        'console_scripts': [
            'uhp = uhp.uhp:main'
        ]
    },
    keywords=['uhp', 'honeypot', 'universal']
)
