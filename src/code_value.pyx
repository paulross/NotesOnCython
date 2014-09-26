cdef extern from "code_value.h":
    int code_0(int value)
    int code_1(int value)
    int code_2(int value)

ctypedef int (*cv_func)(int value)

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
