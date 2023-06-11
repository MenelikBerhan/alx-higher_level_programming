#include <Python.h>

/**
 * print_python_list_info - prints information about a Python list
 * @p: a PyObject pointer to the list
 *
*/
void print_python_list_info(PyObject *p)
{
	int i, len;

	if (!p || p == Py_None || !PyList_Check(p))
		return;

	len = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < len; i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);

}
