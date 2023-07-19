// Индекс относительной силы - RSI (Relative Strength Index)
#include "api.h"


/*
RSI = 100 - [100 / (1 + AU_x / AD_x)]

AU - сумма положительных изменений цены за период
AD - сумма отрицательных изменений цены за период
x - кол-во дней
*/


static PyObject * RSI(PyObject *self, PyObject *args) {
	float AD = 0, AU = 0;

	if (!PyArg_ParseTuple(args, "ff", &AD, &AU)) return NULL;
	float rsi = 100 - (100 / (1 + (AD / AU)));
	return PyLong_FromLong(rsi);
}

static PyMethodDef methods[] = {
	{"RSI", RSI, METH_VARARGS, "RSI"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
	PyModuleDef_HEAD_INIT,
	"API_RSI",
	"API for RSU",
	-1,
	methods
};

PyMODINIT_FUNC
PyInit_API_RSI(void) {
  return PyModule_Create(&module);
}
