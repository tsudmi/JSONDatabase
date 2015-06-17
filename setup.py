#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = [
    'antlr4-python2-runtime==4.5',
    'click==4.0'
]


setup(
    name='json-database',
    version='0.2.0',
    author='Dmitri Chumak',
    author_email='tsudmi@ut.ee',
    url='https://github.com/tsudmi/json-database',
    description='JSON Database is database which holds data in JSON format.',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['json-database=json_database.command_line:main'],
    },
    classifiers=[
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
