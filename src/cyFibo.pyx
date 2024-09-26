# -*- mode:python; coding:utf-8; -*-
# Exploration of Cython's def, cdef and cpdef functions.
# Copyright (C) 2014 Paul Ross
# Paul Ross: cpipdev@googlemail.com


def fib(n):
    """Vanilla Cython."""
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


def fib_int(long n):
    """Vanilla Python with type specification."""
    if n < 2:
        return n
    return fib_int(n-2) + fib_int(n-1)


def fib_cdef(long n):
    """Call a cdef."""
    return fib_in_c(n)


cdef long fib_in_c(long n):
    if n < 2:
        return n
    return fib_in_c(n-2) + fib_in_c(n-1)


cpdef fib_cpdef(long n):
    """Basic cpdef."""
    if n < 2:
        return n
    return fib_cpdef(n-2) + fib_cpdef(n-1)


cpdef long fib_int_cpdef(long n):
    """Typed cpdef."""
    if n < 2:
        return n
    return fib_int_cpdef(n-2) + fib_int_cpdef(n-1)
