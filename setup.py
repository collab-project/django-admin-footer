#!/usr/bin/env python
# Copyright Collab 2015-2016
# See LICENSE for details.

import os
import sys
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# get version nr
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    'admin_footer')))
from admin_footer import version  # flake8: noqa
sys.path.pop(0)

test_deps = [
    "tox",
    "coverage",
    "flake8"
]

setup(
    name='django-admin-footer',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='Templatetag to render footer in Django admin.',
    long_description=README,
    tests_require=test_deps,
    extras_require={
        'docs': [
            'sphinx>=1.5.1'
        ],
        'test': test_deps
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    author='Collab',
    author_email='info@collab.nl',
    url='http://github.com/collab-project/django-admin-footer',
    license='MIT'
)
