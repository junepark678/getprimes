from setuptools import setup
from Cython.Build import cythonize

setup(
    name='getprimes',
    ext_modules=cythonize("getprimes.py"),
    zip_safe=False,
    install_requires=['Cython'],
)

