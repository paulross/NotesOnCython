'''
Created on 21 Jun 2014

@author: paulross
'''
import timeit
import pprint

# import Fibo
# import cyFibo

def pprintDict(d):
    for k in sorted(d.keys()):
        print('%-2s %8s' % (k, d[k]))

def pprintTwoDict(a, b):
    for k in sorted(a.keys()):
        print('%-2s %s %s' % (k, a[k], b[k]))

if __name__ == '__main__':
    siz = 20
    cyFiboResults = {}
    for i in range(siz):
        cyFiboResults[i] = timeit.timeit('cyFibo.fib_cdef(%d)' % i, setup='import cyFibo')
    print('cyFibo Results:')
#     pprint.pprint(cyFiboResults)
#     pprintDict(cyFiboResults)

    FiboResults = {}
    for i in range(siz):
        FiboResults[i] = timeit.timeit('Fibo.fib_cached(%d)' % i, setup='import Fibo')
    print('Fibo Results:')
#     pprint.pprint(FiboResults)
#     pprintDict(FiboResults)
    
    pprintTwoDict(cyFiboResults, FiboResults)
