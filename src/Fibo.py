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

def fib(n):
    """Vanilla Python."""
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def fib_cached(n, cache={}):
    """Cached Python."""
    if n < 2:
        return n
    try:
        val = cache[n]
    except KeyError:
        val = fib(n-2) + fib(n-1)
        cache[n] = val
    return val

