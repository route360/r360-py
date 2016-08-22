from distutils.core import setup
from setuptools import find_packages
setup(
  name = 'r360_py',
  packages = find_packages(), 
  version = '0.2',
  description = 'A python client library to query the Route360° API',
  author = 'Motion Intelligence GmbH',
  author_email = 'mail@motionintelligence.net',
  url = 'https://github.com/route360/r360-py', # use the URL to the github repo
  download_url = 'https://github.com/route360/r360-py/tarball/0.1', # I'll explain this in a second
  keywords = ['isochrone', 'routing', 'polygon', 'openstreetmaps', 'gtfs', 'map'], # arbitrary keywords
  classifiers = [],
)