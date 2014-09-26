#!/usr/bin/env python
# Exploration of Cython's def, cdef and cpdef functions.
# Copyright (C) 2014 Paul Ross
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# 
# Paul Ross: cpipdev@googlemail.com
import os

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

DEBUG = False

extra_compile_args=["-std=c99", ]
if DEBUG:
    extra_compile_args += ["-g3", "-O0", "-DDEBUG=1",]
else:
    extra_compile_args += ["-DNDEBUG", "-Os"]

# /Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/site-packages/numpy/core/include/

# Usage: python3 setup.py build_ext --inplace
setup(
	cmdclass = {'build_ext': build_ext},
	ext_modules = [
		Extension("cyFibo", ["cyFibo.pyx"]),
		Extension(
			"cyStdDev",
			["cyStdDev.pyx", 'std_dev.c'],
			include_dirs = ['/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/site-packages/numpy/core/include/',],
		),
		Extension("cyCodeValue", ["code_value.pyx"]),
		Extension("cFibo", sources=['cFiboExt.c',],
			include_dirs = ['/usr/local/include',], # os.path.join(os.getcwd(), 'include'),],
			library_dirs = [os.getcwd(),],  # path to .a or .so file(s)
			extra_compile_args=extra_compile_args,
		),
		Extension("cyCdefRet", ["cdef_ret.pyx"]),
		Extension("cyClassMethods", ["class_methods.pyx"]),
	]
)
