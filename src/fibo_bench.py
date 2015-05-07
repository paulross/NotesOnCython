from timeit import main as timeit
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
        timeit([
            methods[method].setup,
            methods[method].call])
    for name in methods:
        method = methods[name]
        timer = Timer(method.call.format(30), setup=method.setup)
        print(u"{}: {:g} ms".format(
            name, min(timer.repeat(3, 100)) * 1e3 / 100))


if __name__ == '__main__':
    main()
