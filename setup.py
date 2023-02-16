#!/usr/bin/env python

import os

from setuptools import find_packages, setup

requires = ["sphinx>=4.0"]

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as file:

    setup(
        name="sphinx-rst-table",
        # Update also conf.py and changelog!
        version="0.0.1",
        url="http://github.com/procitec/sphinx-rst-table",
        download_url="http://github.com/procitec/sphinx-rst-table/releases/download/latest/sphinx_rst_table-latest.tar.gz",
        license="MIT",
        author="team procitec",
        author_email="info@procitec.de",
        description="Sphinx extension to create tables with sphinx directives for table, row, columns",
        long_description=file.read(),
        zip_safe=False,
        classifiers=[
            "Framework :: Sphinx",
            "Framework :: Sphinx :: Extension",
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Topic :: Documentation",
        ],
        platforms="any",
        packages=find_packages(),
        include_package_data=True,
        install_requires=requires,
    )
