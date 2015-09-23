from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules=[
    Extension("querycalculate",
              sources=["querycalculate.pyx"],
              libraries=["m"] # Unix-like specific
    )
]

setup(
  name = "querycalculate",
  ext_modules = cythonize(ext_modules)
)