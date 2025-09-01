#!/usr/bin/env python
# Copyright (c) Facebook, Inc. and its affiliates.

from setuptools import setup, Extension

setup(
    name="fb-re2",
    version="1.0.7",
    url="https://github.com/facebook/pyre2",
    description="Python wrapper for Google's RE2",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    author="David Reiss",
    author_email="dreiss@fb.com",
    maintainer="Siddharth Agarwal",
    maintainer_email="sid0@fb.com",
    py_modules = ["re2"],
    test_suite = "tests",
    ext_modules = [Extension("_re2",
      sources = ["_re2.cc"],
      libraries = ["re2"],
      extra_compile_args=['-std=c++11'],
      )],
    )
