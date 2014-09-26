# File: pyClassMethods.py

class PyA(object):

    def d(self): return 0
    
    def test_d(self, num):
        while num > 0:
            self.d()
            num -= 1

class PyB(PyA): pass    
            