import importlib
import os
import sys

import setuptools

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(path, 'source'))

flux = importlib.import_module('flux')

setuptools.setup(
  name=flux.__title__,
  version=flux.__version__,
  author=flux.__author__,
  description=flux.__description__,
  license=flux.__license__,
  url=flux.__url__,
  packages=flux.__packages__,
  package_dir={
    '': 'source'
  },
)
