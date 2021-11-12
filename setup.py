from distutils.core import setup
from setuptools import find_packages

setup(name='le65dyem', 
      version= '0.1', 
      autor='Daniel Augsburger', 
      author_email = 'daniel.augsburger@fau.de', 
      packages = find_packages(),
      install_requires = ['numpy', 'Pillow', 'ipywidgets'])

     
