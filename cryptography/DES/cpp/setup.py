from distutils.core      import setup
from distutils.extension import Extension

import os.path

path_prefix = os.path.dirname(__file__)

files = ["_des.cpp"]
files = [os.path.join(path_prefix, member) for member in files]

_des = Extension(
    '_des',
    sources=files,
    libraries=['boost_python3'],
    extra_compile_args=['-std=c++11']
)

setup(
    name='DES',
    version='0.1',
    ext_modules=[_des]
)