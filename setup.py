from setuptools import setup, find_packages
from hiscore import __version__, __maintainer__, __email__

long_description = open('README.md').read()

install_requires = [
  'numpy',
  'gurobipy'
]

setup(
  name = 'hiscore',
  version = __version__,
  author = __maintainer__,
  author_email = __email__,
  packages = find_packages(),
  description = 'A simple and powerful engine for creating scores',
  long_description=long_description,
  install_requires=install_requires,
  url = 'https://github.com/aothman/hiscore', # use the URL to the github repo
  download_url = "https://github.com/aothman/hiscore/tarball/"+__version__,
  keywords = [],
  classifiers =[],
)
