from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksStorageManager',
    version='0.0.1',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Geobricks storage manager.',
    install_requires=[
        'GeobricksCommon',
    ],
    url='http://pypi.python.org/pypi/GeobricksStorageManager/',
    keywords=['geobricks', 'metadata', 'geoserver', 'd3s']
)
