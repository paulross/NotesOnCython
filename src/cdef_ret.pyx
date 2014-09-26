
def call(val):
    return _cdef(val)

cdef int _cdef(int val):
    raise ValueError('Help')
    return val + 200
