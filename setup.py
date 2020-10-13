from skbuild import setup
import setuptools

setup(
    name="prototype_lib_4_bindings",
    version="0.0.0",
    author="Massimiliano Galli",
    author_email="massimiliano.galli.95@gmail.com",
    description="Prototype to test pythonization of C++ libraries with Cppyy included in ROOT",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    #url="https://github.com/maxgalli/ntupro",
    packages=setuptools.find_packages(),
    #cmake_install_dir = 'cmake',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
