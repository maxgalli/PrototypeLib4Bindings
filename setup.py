from distutils.core import setup
import setuptools
from importlib import import_module

# Check ROOT related requirements and raise error if not found
for pkg in ['ROOT', 'cppyy', 'cppyy_backend']:
    try:
        import_module(pkg)
    except ModuleNotFoundError:
        raise ImportError('{} not found. You need a full working installation of ROOT to install this package. \
                For more info, see: https://root.cern/install/')

setup(
    name="prototype_lib_4_bindings",
    version="0.0.0",
    author="Massimiliano Galli",
    author_email="massimiliano.galli.95@gmail.com",
    description="Prototype to test pythonization of C++ libraries with Cppyy included in ROOT",
    #long_description=,
    #long_description_content_type="text/markdown",
    url="https://github.com/maxgalli/PrototypeLib4Bindings",
    packages=setuptools.find_packages(),
    #cmake_install_dir = ,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #install_requires = ['ROOT', 'cppyy', 'cppyy_backend'], it would be nice if it could work
    python_requires='>=3.6',
)
