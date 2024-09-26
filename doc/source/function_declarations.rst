.. highlight:: python
    :linenothreshold: 10

.. toctree::
    :maxdepth: 3

==============================================================
Cython Function Declarations
==============================================================

Cython supports three ways of declaring functions using the keywords: ``def``, ``cdef`` and ``cpdef``.

``def`` - Basically, it's Python
--------------------------------
``def`` is used for code that:

* Will be called directly from Python code with Python objects as arguments.
* Returns a Python object.

The generated code treats every operation as if it was dealing with Python objects with Python consequences so it incurs a high overhead. ``def`` is safe to use with no gotchas. Declaring the types of arguments and local types (thus return values) can allow Cython to generate optimised code which speeds up the execution. If the types are declared then a ``TypeError`` will be raised if the function is passed the wrong types.

``cdef`` - Basically, it's C
--------------------------------
``cdef`` is used for Cython functions that are intended to be pure 'C' functions. All types *must* be declared. Cython aggressively optimises the code and there are a number of gotchas. The generated code is about as fast as you can get though.

``cdef`` declared functions are not visible to Python code that imports the module.

Take some care with ``cdef`` declared functions; it looks like you are writing Python but actually you are writing C.

``cpdef`` - It's Both
----------------------------
``cpdef`` functions combine both ``def`` and ``cdef`` by creating two functions; a ``cdef`` for C types and a ``def`` for Python types. This exploits early binding so that ``cpdef`` functions may be as fast as possible when using C fundamental types (by using ``cdef``). ``cpdef`` functions use dynamic binding when passed Python objects and this might much slower, perhaps as slow as ``def`` declared functions.
