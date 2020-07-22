from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'steganocryptopy',
  packages = ['steganocryptopy'],
  version = '0.1.1',
  license='MIT',
  description = 'The simplest Python Steganography with crypto out there!',
  author = 'K V Vignesh',
  author_email = 'vigneshkundhanam@gmail.com',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url = 'https://github.com/kvvignesh/steganocryptopy',
  download_url = 'https://github.com/kvvignesh/steganocryptopy/archive/v1.0.tar.gz',
  keywords = ['Steganography', 'crypto', 'encrypt'],
  install_requires=['click', 'cryptography', 'Pillow'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)