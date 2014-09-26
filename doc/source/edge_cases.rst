.. highlight:: python
    :linenothreshold: 100

.. toctree::
    :maxdepth: 3

==============================================================
``cdef``'ing to a SEGFAULT
==============================================================

Here is an edge case simplified from an issue with `Pandas, issue 4519 <https://github.com/pydata/pandas/issues/4519>`_. Suppose we have a number of C functions that return different variations of their arguments:

.. code-block:: c

    /* File: code_value.h */

    int code_0(int value) {
        return value + 0;
    }

    int code_1(int value) {
        return value + 1;
    }

    int code_2(int value) {
        return value + 2;
    }

This is then called from this Cython code:

.. code-block:: cython

    # File: code_value.pyx

    cdef extern from "code_value.h":
        int code_0(int value)
        int code_1(int value)
        int code_2(int value)

    ctypedef int (*cv_func)(int value)

    # Given an integer code this returns the appropriate function or raises ValueError
    cdef cv_func get_func(int code):
        if code == 0:
            return &code_0
        elif code == 1:
            return &code_1
        elif code == 2:
            return &code_2
        else:
            raise ValueError('Unrecognised code: %s' % code)
    
    def code_value(int code, int value):
        cdef:
            cv_func f
        
        f = get_func(code)
        return f(value)

This all works fine until we provide a code that is out of range::

    >>> import cyCodeValue
    >>> cyCodeValue.code_value(0, 10)
    10
    >>> cyCodeValue.code_value(1, 10)
    11
    >>> cyCodeValue.code_value(2, 10)
    12
    >>> cyCodeValue.code_value(3, 10)
    Exception ValueError: ValueError('Unrecognised code: 3',) in 'cyCodeValue.get_func' ignored
    Segmentation fault: 11

If we look at the C code that Cython has generated we can see what is going on, I have edited and annotated the code for clarity:

.. code-block:: c

        /* "code_value.pyx":16
         *         return &code_2
         *     else:
         *         raise ValueError('Unrecognised code: %s' % code)             # <<<<<<<<<<<<<<
         * 
         */

        __pyx_t_2 = __Pyx_PyObject_Call(__pyx_builtin_ValueError, __pyx_t_1, NULL);
        ...
        __pyx_filename = __pyx_f[0];
        __pyx_lineno = 16;
        __pyx_clineno = __LINE__;
        goto __pyx_L1_error;
      }

      /* function exit code */
      __pyx_L1_error:; /* We land here after the ValueError. */
      ...
      __Pyx_WriteUnraisable("cyCodeValue.get_func", __pyx_clineno, __pyx_lineno, __pyx_filename, 0);
      __pyx_r = 0;
      __pyx_L0:;
      __Pyx_RefNannyFinishContext();
      return __pyx_r;
    }

``get_func()`` is declared as a ``cdef`` that returns a fundamental C type, a function pointer. This suppresses any Python Exception with the call to ``__Pyx_WriteUnraisable``, in that case ``get_func()`` returns 0 which, when dereferenced, causes the SEGFAULT.

``cdef`` Exceptions and the Return Type
------------------------------------------

The Cython documentation says "...a function declared with cdef that does not return a Python object has no way of reporting Python exceptions to its caller. If an exception is detected in such a function, a warning message is printed and the exception is ignored."

Lets see this in isolation::

    # File: cdef_ret.pyx
    
    def call(val):
        return _cdef(val)

    cdef int _cdef(int val):
        raise ValueError('Help')
        return val + 200

The ``ValueError`` will be created, reported, destroyed and the function will return from the *exception* point and the return statement will never be executed. The return value will be the default for the return type, in this case 0::

    >>> import cyCdefRet
    >>> cyCdefRet.call(7)
    Exception ValueError: ValueError('Help',) in 'cyCdefRet._cdef' ignored
    0
 
The situation changes if we change the declaration of ``_cdef()`` to::

    # File: cdef_ret.pyx
    
    def call(val):
        return _cdef(val)

    cdef _cdef(int val):
        raise ValueError('Help')
        return val + 200

In the absence of a return type then Cython assumes a *Python return type* of None so now the exception is *not* ignored and we get::

    >>> import cyCdefRet
    >>> cyCdefRet.call(7)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "cdef_ret.pyx", line 3, in cyCdefRet.call (cdef_ret.c:718)
        return _cdef(val)
      File "cdef_ret.pyx", line 6, in cyCdefRet._cdef (cdef_ret.c:769)
        raise ValueError('Help')
    ValueError: Help

If you really want a ``cdef`` that returns void then declare it as ``cdef _cdef(int val):``



