#ifndef EXTENDS_TESTER_API_H_
#define EXTENDS_TESTER_API_H_
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

#if PY_MAJOR_VERSION >= 3

// Extentions
static PyObject * RSI(PyObject *, PyObject *);

#endif

#endif // EXTENDS_TESTER_API_H_