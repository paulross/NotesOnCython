Performance of Cython Classes using ``def``, ``cdef`` and ``cpdef``
===========================================================================

Here we have a class ``A`` with the three differenct types of method declarations and some means of exercising each one::

    # File: class_methods.pyx

    cdef class A(object):

        def       d(self): return 0
        cdef  int c(self): return 0
        cpdef int p(self): return 0
    
        def test_def(self, long num):
            while num > 0:
                self.d()
                num -= 1
            
        def test_cdef(self, long num):
            while num > 0:
                self.c()
                num -= 1
            
        def test_cpdef(self, long num):
            while num > 0:
                self.p()
                num -= 1

We can time the execution of these thus with 1e6 calls::

    $ python3 -m timeit -s "import cyClassMethods" -s "a = cyClassMethods.A()" "a.test_def(1000000)"
    $ python3 -m timeit -s "import cyClassMethods" -s "a = cyClassMethods.A()" "a.test_cdef(1000000)"
    $ python3 -m timeit -s "import cyClassMethods" -s "a = cyClassMethods.A()" "a.test_cpdef(1000000)"


============  =============  ====================
Call          Result (ms)    Compared to ``cdef``
============  =============  ====================
A def         35.9           x17
A cdef        2.15           x1
A cpdef       3.19           x1.5
============  =============  ====================

The Effect of Sub-classing
-----------------------------

If we now subclass ``A`` to ``B`` where ``B`` is merely ``class B(cyClassMethods.A): pass`` and time that::


    $ python3 -m timeit -s "import cyClassMethods" -s "class B(cyClassMethods.A): pass" -s "b = B()" "b.test_def(1000000)"
    $ python3 -m timeit -s "import cyClassMethods" -s "class B(cyClassMethods.A): pass" -s "b = B()" "b.test_cdef(1000000)"
    $ python3 -m timeit -s "import cyClassMethods" -s "class B(cyClassMethods.A): pass" -s "b = B()" "b.test_cpdef(1000000)"

============  =============  ====================
Call          Result (ms)    Compared to ``cdef``
============  =============  ====================
B def         42.6           x20
B cdef        2.17           x1
B cpdef       37.2           x17
============  =============  ====================

We can compare these results with a pure Python implemention::

    # File: pyClassMethods.py

    class PyA(object):

        def d(self): return 0
    
        def test_d(self, num):
            while num > 0:
                self.d()
                num -= 1

    class PyB(A): pass    

Which we can time with::

    $ python3 -m timeit -s "import pyClassMethods" -s "a = pyClassMethods.PyA()" "a.test_d(1000000)"
    10 loops, best of 3: 180 msec per loop
    $ python3 -m timeit -s "import pyClassMethods" -s "b = pyClassMethods.PyB()" "b.test_d(1000000)"
    10 loops, best of 3: 182 msec per loop

Compared with the Cython ``cdef`` function these are x84 and x85 respectively.

Graphically the comparison looks like this (note log scale):

.. image:: images/Classes.png

My conclusions:

* Cython gives around x4 improvement for normal ``def`` method calls.
* ``cdef`` method calls of Cython classes, or those deriving from them, can give a x80 or so performance improvement over pure Python.
* ``cpdef`` holds up well as a 'safe' ``cdef`` unless subclassing is used when the cost of the (Python) method lookup brings ``cpdef`` back to ``def`` level.
