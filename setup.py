#! /usr/bin/env python
"""
Author: Jeremy M. Stober
Program: SETUP.PY
Date: Saturday, February 25 2012
Description: Install simple cartpole simulation.
"""
from distutils.core import setup

setup(name='td',
      version='0.01',
      description='Cartpole Simulation in Python',
      author="Jeremy Stober",
      author_email="stober@gmail.com",
      package_dir={"cartpole" : "src"},
      packages=["cartpole"]
      )
