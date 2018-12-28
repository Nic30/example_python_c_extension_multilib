
from setuptools.extension import Library, Extension
from setuptools import setup
from distutils.sysconfig import get_config_var


# "cpython-36m-x86_64-linux-gnu"
SOABI = get_config_var("SOABI")
# e.g. "linux"
MACHDEP = get_config_var("MACHDEP")
# e.g. "x86_64"
AR = get_config_var("AR").split("-")[0]
# e.g. "3.6"
VERSION = get_config_var("VERSION")

ACTUAL_LIB_DIR = "build/lib.%s-%s-%s" % (MACHDEP, AR, VERSION)

lib0 = Library("lib0",
               sources=["lib0/lib0.cpp"])

ext0 = Extension("_ext0",
                 sources=["ext0/ext0.cpp"],
                 include_dirs=["lib0/"],
                 libraries=["lib0." + SOABI],
                 library_dirs=[ACTUAL_LIB_DIR]
                 )

setup(
    name='exampe_setuptools',
    version='1.2',
    author='Michal Orsak',
    author_email='michal.o.socials@gmail.com',
    ext_modules=[lib0, ext0],
)
