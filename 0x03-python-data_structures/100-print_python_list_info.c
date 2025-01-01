#include <Python.h>

/**
* print_python_list_info - prints some basic info about Python lists
* @p: a Python object representing a list
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		PyErr_SetString(PyExc_TypeError, "Provided object is not a list");
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i); /* Borrowed reference */
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
