#!/usr/bin/env python

import os
import re
import sys

from codecs import open

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# 'setup.py publish' shortcut.


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

about = {}
with open(os.path.join(here, 'instana', '__version__.py')) as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=[
        'instana',
        'instana.collections',
        'instana.models',
    ],
    package_data={'': ['LICENSE', 'NOTICE'], 'instana': ['*.pem']},
    package_dir={'instana': 'instana'},
    include_package_data=True,
    install_requires=['requests'],
    license=about['__license__'],
    zip_safe=False,
    keywords='instagram private api',
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ),
    test_suite='nose.collector',
    tests_require=['nose'],
)
