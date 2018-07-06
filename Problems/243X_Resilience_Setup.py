# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 22:56:39 2018

@author: PaulJ
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize


"""
ext_modules = [Extension('find_fastest_time_cython',
                         ['find_fastest_time_cython.pyx'],
                         # libraries=['m'],
                         # extra_compile_args=['-ffast-math']
                         
                         )]
"""
ext_modules = cythonize(r'p243_Resilience_cython.pyx')

setup(
    name='p243_Resilience_cython',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules)
