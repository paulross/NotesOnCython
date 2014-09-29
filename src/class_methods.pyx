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
