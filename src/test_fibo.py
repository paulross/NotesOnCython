import unittest

from Fibo import fib, fib_cached
from cFibo import fib as cfib
from cyFibo import fib as cyfib
from cyFibo import fib_cdef, fib_int, fib_cpdef, fib_int_cpdef


class TestFibo(unittest.TestCase):

    def _check_fibonacci(self, function):
        expected = [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        result = [function(i) for i in range(13)]
        self.assertEqual(expected, result)

    def test_fib(self):
        self._check_fibonacci(fib)

    def test_cfib(self):
        self._check_fibonacci(cfib)

    def test_cyfib(self):
        self._check_fibonacci(cyfib)

    def test_fib_cdef(self):
        self._check_fibonacci(fib_cdef)

    def test_fib_cpdef(self):
        self._check_fibonacci(fib_cpdef)

    def test_fib_int_cpdef(self):
        self._check_fibonacci(fib_int_cpdef)

    def test_fib_int(self):
        self._check_fibonacci(fib_int)

    def test_fib_cached(self):
        self._check_fibonacci(fib_cached)
