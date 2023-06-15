#include <Python.h>

/**
 * print_python_bytes - prints information about a Python byte object
 * @p: a PyObject pointer to the list
 *
*/
void print_python_bytes(PyObject *p)
{
	int i, len;
	char *str, end;

	if (!p || p == Py_None)
		return;
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = PyBytes_Size(p);
	printf("  size: %d\n", len);
	str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str);
	printf("  first %d bytes: ", len > 9 ? 10 : len + 1);
	for (i = 0; i < 10 && i <= len; i++)
	{
		if (i == 9 || i == len)
			end = '\n';
		else
			end = ' ';
		printf("%.2x%c", str[i], end);
	}

}

/**
 * print_python_list - prints information about a Python list object
 * @p: a PyObject pointer to the list
 *
*/
void print_python_list(PyObject *p)
{
	int i, len;
	const char *type;

	if (!p || p == Py_None || !PyList_Check(p))
		return;
	printf("[*] Python list info\n");
	len = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < len; i++)
	{
		type = PyList_GET_ITEM(p, i)->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (!strncmp(type, "bytes", 5))
			print_python_bytes(PyList_GET_ITEM(p, i));
	}
}
