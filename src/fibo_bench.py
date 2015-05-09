from timeit import Timer
from timeit import main as console_timeit
from collections import namedtuple, OrderedDict

Bench = namedtuple('Bench', ['setup', 'call'])


methods = OrderedDict([
    ('Python', Bench("import Fibo", "Fibo.fib({})")),
    ('Cython naive', Bench("import cyFibo", "cyFibo.fib({})")),
    ('Cython typed', Bench("import cyFibo", "cyFibo.fib_int({})")),
    ('Cython cdef', Bench("import cyFibo", "cyFibo.fib_cdef({})")),
    ('Cython cpdef', Bench("import cyFibo", "cyFibo.fib_cpdef({})")),
    ('Cython typed cpdef',
        Bench("import cyFibo", "cyFibo.fib_int_cpdef({})")),
    ('Wrapped C', Bench("import cFibo", "cFibo.fib({})")),
    ('Python alt', Bench("import Fibo", "Fibo.fib_cached({})"))])


def main():
    for method in methods:
        print(method)
        console_timeit([
            methods[method].setup,
            methods[method].call.format(30)])

if __name__ == '__main__':
    main()
