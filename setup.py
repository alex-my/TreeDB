#!/usr/bin/env python
# coding:utf8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog', '')


setup(
    name='TreeDB',
    version='0.0.2',
    description='be easy to use mysql driver.',
    long_description=readme + '\n\n' + history,
    author='Alex',
    author_email='alex_my@126.com',
    url='git@github.com:alex-my/TreeDB.git',
    packages=['TreeDB'],
    include_package_data=True,
    install_requires=[],
    license='MIT',
    zip_safe=False,
    keywords='TreeDB',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ]
)
