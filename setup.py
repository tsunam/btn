import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='btn',
      version='0.0.1',
      description='A broadcasthe.net api client',
      long_description=read('README.md'),
      author='Joshua Jackson',
      author_email='tsunam@gmail.com',
      packages=['btn'],
      python_requires=">=3.5",
      install_requires=['jsonrpc-requests>=0.4.0'],
      license='GPLv3',
      keywords='api broadcasthenet',
      classifiers=[
          'Development Status :: 4 - Beta', 'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8'
      ])
