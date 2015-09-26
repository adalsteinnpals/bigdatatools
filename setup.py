from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

ext_modules=[
    Extension("querycalculate",
              sources=["querycalculate.pyx"],
              libraries=["m"], # Unix-like specific
              extra_compile_args=['-fopenmp'],
            extra_link_args=['-fopenmp'],
    )
]

setup(
  name = "querycalculate",
  cmdclass = {'build_ext': build_ext},
  ext_modules = cythonize(ext_modules)
)