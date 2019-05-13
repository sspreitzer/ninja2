from setuptools import setup, find_packages

setup(
      name = 'ninja2',
      version = '0.2',
      description = 'Jinja2 command line client',
      url = 'https://github.com/sspreitzer/ninja2',
      download_url = 'https://github.com/sspreitzer/ninja2/tarball/0.2',
      author = 'Sascha Spreitzer',
      author_email = 'sascha@spreitzer.ch',
      license = 'MIT',
      classifiers = [
                     'Environment :: Console',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                     'Development Status :: 4 - Beta',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 3',
                     'Topic :: Utilities'
                     ],
      keywords = 'ninja2 jinja2 python json yaml',
      install_requires = ['Jinja2'],
      scripts = ['ninja2'],
)

