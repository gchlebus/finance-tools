# -*- coding: utf-8 -*-

__author__ = 'gchlebus'

from setuptools import setup, find_packages

setup(
  name='finance-tools',
  version='0.1',
  author='Grzegorz Chlebus',
  url='https://github.com/gchlebus/finance-tools',
  license='BSD 3-Clause',
  author_email='gchlebus@gmail.com',
  packages=find_packages(exclude=['test']),
  install_requires=['click', 'pandas'],
  entry_points='''
    [console_scripts]
    ft=finance_tools.cli:cli
  '''
)
