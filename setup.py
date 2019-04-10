#nsml: nsml/pytorch:0.3.0-cuda8cudnn6-konlpy0.4-py3.6

try:
 from setuptools import setup, install_requires
except ImportError:
 from distutils.core import setup, install_requires
setup(
    name='AQM',
    version='1.0',
    install_requires = [
      'visdom',
      'markdown2',
      'nltk'
    ]
)
