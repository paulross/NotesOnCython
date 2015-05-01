from timeit import main as timeit
from collections import namedtuple, OrderedDict

Bench = namedtuple('Bench', ['setup', 'call'])


methods = OrderedDict([
    ('Python', Bench("import Fibo", "Fibo.fib(30)")),
    ('Cython naive', Bench("import cyFibo", "cyFibo.fib(30)")),
    ('Cython typed', Bench("import cyFibo", "cyFibo.fib_int(30)")),
    ('Cython cdef', Bench("import cyFibo", "cyFibo.fib_cdef(30)")),
    ('Cython cpdef', Bench("import cyFibo", "cyFibo.fib_cpdef(30)")),
    ('Cython typed cpdef',
        Bench("import cyFibo", "cyFibo.fib_int_cpdef(30)")),
    ('Wrapped', Bench("import cFibo", "cFibo.fib(30)")),
    ('Python alt', Bench("import Fibo", "Fibo.fib_cached(30)"))])


def main():
    for method in methods:
        print(method)
        timeit([
            methods[method].setup,
            methods[method].call])

if __name__ == '__main__':
    main()
