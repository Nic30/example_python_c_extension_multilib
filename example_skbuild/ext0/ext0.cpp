#include "lib0.h"
#include <Python.h>

static PyObject *module_func_add(PyObject *self, PyObject *args) {
	int a, b;
	if(!PyArg_ParseTuple(args, "ii", &a, &b)) {
			return nullptr;
	}

	return PyLong_FromLong(add(a, b));
}

static PyMethodDef module_methods[] = {
   { "add", (PyCFunction)module_func_add, METH_VARARGS, NULL },
   { NULL, NULL, 0, NULL }
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "_ext0",     /* m_name */
    "This is a module",  /* m_doc */
    -1,                  /* m_size */
	module_methods,    /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
};

PyMODINIT_FUNC PyInit__ext0() {
	auto m = PyModule_Create(&moduledef);
	if (m == nullptr)
		return nullptr;

	return m;
}
