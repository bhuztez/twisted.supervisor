#!/usr/bin/env python2

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='twisted.supervisor',
    version='0.0',

    url='',
    description='Twisted supervisor',

    classifiers = [
        "Development Status :: 1 - Planning",
        "Environment :: No Input/Output (Daemon)",
        "Framework :: Twisted",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7"
        "Topic :: System :: Boot",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration",
    ],

    author='bhuztez',
    author_email='bhuztez@gmail.com',

    requires=['Twisted (>= 11.0)'],

    namespace_packages=['twisted'],
    packages = ['twisted', 'twisted.supervisor'],
    package_data={
        'twisted': ['plugins/twisted_supervisor.py'],
    },

    zip_safe = False,
)


