#include "Python.h"

/* This is the function that actually computes the Fibonacci value. */
static long c_fibonacci(long ord) {
	if (ord < 2) {
		return ord;
	}
	return c_fibonacci(ord - 2) + c_fibonacci(ord -1);
}

/* The Python interface to the C code. */
static PyObject *python_fibonacci(PyObject *module, PyObject *arg) {
    PyObject *ret = NULL;
    assert(arg);
    Py_INCREF(arg);
    if (! PyLong_CheckExact(arg)) {
    	PyErr_SetString(PyExc_ValueError, "Argument is not an integer.");
    	goto except;
    }
    long ordinal = PyLong_AsLong(arg);
    long result = c_fibonacci(ordinal);
    ret = PyLong_FromLong(result);
    assert(! PyErr_Occurred());
    assert(ret);
    goto finally;
except:
    Py_XDECREF(ret);
    ret = NULL;
finally:
    Py_DECREF(arg);
    return ret;
}

/********* The rest is standard Python Extension code ***********/


static PyMethodDef cFiboExt_methods[] = {
  {"fib", python_fibonacci, METH_O, "Fibonacci value."},
  {NULL, NULL, 0, NULL}           /* sentinel */
};


#if PY_MAJOR_VERSION >= 3

/********* PYTHON 3 Boilerplate ***********/

PyDoc_STRVAR(module_doc, "Fibonacci in C.");

static struct PyModuleDef cFiboExt = {
  PyModuleDef_HEAD_INIT,
  "cFibo",
  module_doc,
  -1,
  cFiboExt_methods,
  NULL,
  NULL,
  NULL,
  NULL
};

PyMODINIT_FUNC
PyInit_cFibo(void)
{
  return PyModule_Create(&cFiboExt);
}

#else

/********* PYTHON 2 Boilerplate ***********/


PyMODINIT_FUNC
initcFibo(void)
{
  (void) Py_InitModule("cFibo", cFiboExt_methods);
}

#endif
