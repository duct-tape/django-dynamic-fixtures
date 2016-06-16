import os

from setuptools import setup, find_packages

VERSION = '0.1.2'

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-dynamic-fixtures',
    version=VERSION,
    long_description=README,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    extras_require={
        'dev': [
            'bumpversion==0.5.3',
            'twine == 1.6.5',
        ],
        'doc': [
            'Sphinx==1.4.4',
            'sphinx-autobuild==0.6.0',
        ]
    },
    setup_requires=[
        'pytest-runner'
    ],
    install_requires=[
        'Django>=1.7,<=1.8'
    ],
    tests_require=[
        'pytest-django',
        'mock>=2.0',
    ],
    url='https://github.com/Peter-Slump/django-dynamic-fixtures',
    license='MIT',
    author='Peter Slump',
    author_email='peter@yarf.nl',
    description='Install Dynamic Django fixtures.'
)
