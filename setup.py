# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Jason Beach',
    author_email='information@mgmt-tech.org',
    url='https://github.com/IMTorgDemo/Boilerplate-Python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
      package_data={'': ['data.file']},
      scripts=['bin/sample'],
      include_package_data=True,
      zip_safe=False
)

