#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests',
]

test_requirements = [
    'responses',
    'pytest',
    'coverage',
    'responses',
    'coverage',
]

setup(
    name='pydrill',
    version='0.0.1',
    description="Python Driver for Apache Drill.",
    long_description=readme + '\n\n' + history,
    author="Wojciech Nowak",
    author_email='mail@pythonic.ninja',
    url='https://github.com/PythonicNinja/pydrill',
    packages=[
        'pydrill',
    ],
    package_dir={'pydrill':
                 'pydrill'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='pydrill',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
