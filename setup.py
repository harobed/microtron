#! /usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


classifiers = """\
Development Status :: 3 - Alpha
Environment :: Console
Intended Audience :: Information Technology
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
"""

setup(
    name='Microtron',
    version='0.16',
    description='Microformats parser',
    author='Andrew McCollum',
    author_email='amccollum@gmail.com',
    license='MIT',
    url='http://github.com/amccollum/microtron',
    install_requires=[
        'lxml >= 2.2.2',
        'isodate >= 0.4.0',
    ],
    package_data={'': ['*.xml']},
    packages=find_packages(exclude=['ez_setup']),
    zip_safe=False,
    entry_points="""
    [console_scripts]
    microtron-parse = microtron.scripts:parse
    microtron-check = microtron.scripts:check
    """,
)
