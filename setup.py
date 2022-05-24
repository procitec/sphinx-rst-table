#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

requires = ['sphinx>4.0']

setup(
    name='sphinxcontrib-rst-table',
    version='0.0.1',
    url='https://github.com/procitec/sphinxcontrib-rst-table.git',
    download_url='https://github.com/procitec/sphinxcontrib-rst-table.git',
    license='MIT',
    author='team procitec',
    author_email='info@procitec.de',
    description='Sphinx extension for creation of tables with Sphinx/ReST directives',
    long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Documentation',
        'Topic :: Utilities',
        'Framework :: Sphinx :: Extension',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
