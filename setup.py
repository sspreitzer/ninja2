from setuptools import setup, find_packages

setup(
      name = 'j2',
      version = '0.1',
      description = 'Jinja2 command line client',
      url = 'https://github.com/sspreitzer/j2',
      author = 'Sascha Spreitzer',
      author_email = 'sascha@spreitzer.ch',
      license = 'MIT',
      classifiers = [
                     'Development Status :: 2 - Beta',
                     'Programming Language :: Python :: 2',
                     ],
      keywords = 'j2 jinja2 python json yaml',
      install_requires = ['Jinja2'],
      scripts = ['j2'],
)

