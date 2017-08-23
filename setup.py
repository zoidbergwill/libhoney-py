import sys
from setuptools import find_packages, setup
sys.path.append('libhoney/')
from version import VERSION


setup(name='libhoney',
      version=VERSION,
      description='Python library for sending data to Honeycomb',
      url='https://github.com/honeycombio/libhoney-py',
      author='Honeycomb.io',
      author_email='feedback@honeycomb.io',
      license='Apache',
      packages=find_packages(),
      install_requires=[
          'requests',
          'statsd',
          'six',
      ],
      tests_require=[
        'mock',
        'pbr',
        'requests-mock',
        'bumpversion'
      ],
      test_suite='libhoney',
      zip_safe=False)
