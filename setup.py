from setuptools import setup, find_packages

setup(
      name = 'ninja2',
      version = '0.1',
      description = 'Jinja2 command line client',
      url = 'https://github.com/sspreitzer/ninja2',
      download_url = 'https://github.com/sspreitzer/ninja2/tarball/0.1',
      author = 'Sascha Spreitzer',
      author_email = 'sascha@spreitzer.ch',
      license = 'MIT',
      classifiers = [
                     'Development Status :: 4 - Beta',
                     'Programming Language :: Python :: 2',
                     ],
      keywords = 'ninja2 jinja2 python json yaml',
      install_requires = ['Jinja2'],
      scripts = ['ninja2'],
)

