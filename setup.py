from distutils.core import setup
setup(
  name = 'figdataloader',
  packages = ['figdataloader'],
  version = '0.1.5',
  license='MIT',
  description = 'Easy data loading for figure detection neural networks.',
  author = 'Luis Gómez',
  author_email = 'luisgom99@hotmail.com',
  url = 'https://github.com/SilentTyp3',
  download_url = 'https://github.com/SilentTyp3/figdataloader/archive/refs/tags/data.tar.gz',
  keywords = ['DATA', 'LOAD', 'FIGURES'],
  install_requires=[
          'numpy',
          'promptlib',
          'pathlib',
          'Pillow',
          'imutils',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)