from setuptools import setup, Extension
import sys
import numpy

setup(name          = 'fasttrips',
      version       = '1.0a1',
      author        = 'MTC, SFCTA & PSRC',
      author_email  = 'lzorn@mtc.ca.gov',
      description   = 'Dynamic Transit Assignment Model. Given a transit network and a list of transit demand, finds a pathset and chooses a path for each traveler.',
      packages      = ['fasttrips'],
      url           = 'http://fast-trips.mtc.ca.gov/',
      license       = 'Apache',
      classifiers   = [# How mature is this project?
                       'Development Status :: 3 - Alpha',

                       # Indicate who your project is intended for
                       'Intended Audience :: Other Audience',
                       'Topic :: Scientific/Engineering',

                       # Pick your license as you wish (should match "license" above)
                        'License :: OSI Approved :: Apache Software License',

                       # Specify the Python versions you support here. In particular, ensure
                       # that you indicate whether you support Python 2, Python 3 or both.
                       'Programming Language :: Python :: 2',
                       'Programming Language :: Python :: 2.7'],
      keywords      = 'transit model dynamic passenger assignment simulation',
      install_requires = ['pandas','transitfeed'],
      package_data  = { 'Examples':['Examples'] },
      ext_modules   = [Extension('_fasttrips',
                                 sources=['src/fasttrips.cpp',
                                          'src/hyperlink.cpp',
                                          'src/access_egress.cpp',
                                          'src/path.cpp',
                                          'src/pathfinder.cpp',
                                          ],
                                 include_dirs=[numpy.get_include()],
                                 libraries=['psapi'] if sys.platform=='win32' else []
                                 )
                      ],
      )