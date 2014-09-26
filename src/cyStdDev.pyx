# -*- mode:python; coding:utf-8; -*-
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
"""
Created on 21 Jun 2014

@author: paulross
"""
import math

def cyStdDev(a):
    m = a.mean()
    w = a - m
    wSq = w**2
    return math.sqrt(wSq.mean())

cdef extern from "math.h":
    double sqrt(double m)

from numpy cimport ndarray
cimport numpy as np
cimport cython

@cython.boundscheck(False)
def cyOptStdDev(ndarray[np.float64_t, ndim=1] a not None):
    cdef Py_ssize_t i
    cdef Py_ssize_t n = a.shape[0]
    cdef double m = 0.0
    for i in range(n):
        m += a[i]
    m /= n
    cdef double v = 0.0
    for i in range(n):
        v += (a[i] - m)**2
    return sqrt(v / n)

cdef extern from "std_dev.h":
    double std_dev(double *arr, size_t siz)
    
def cStdDev(ndarray[np.float64_t, ndim=1] a not None):
    return std_dev(<double*> a.data, a.size)
