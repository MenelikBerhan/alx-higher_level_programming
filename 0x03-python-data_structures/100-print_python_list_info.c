#include <Python.h>

/**
 * print_python_list_info - prints information about a Python list
 * @p: a PyObject pointer to the list
 *
*/
void print_python_list_info(PyObject *p)
{
	int i, len;
	static int alloc_ed = -1;
	static PyObject *temp;

	if (!p || p == Py_None || !PyList_Check(p))
		return;
	len = PyList_Size(p);
	if (alloc_ed == -1 || p != temp)
		alloc_ed = len;
	else if (len > alloc_ed)
		alloc_ed  = len + (len >> 3) + (len < 9 ? 3 : 6);

	temp = p;
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", alloc_ed);

	for (i = 0; i < len; i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);

}
