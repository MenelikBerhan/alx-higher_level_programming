#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - prints information about a Python floating point object
 * @p: a PyObject pointer to a a Python floating point object
 *
*/
void print_python_float(PyObject *p)
{
	int size, i;
	char *float_as_str;

	if (!p || p == Py_None)
		return;
	printf("[.] float object info\n");
	fflush(stdout);
	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}
	size = snprintf(NULL, 0, "%.15lf", (PyFloat_AsDouble(p)));
	float_as_str = malloc(size + 1);
	sprintf(float_as_str, "%.15lf", (PyFloat_AsDouble(p)));
	for (i = size; i > 0; i--)
	{
		if (float_as_str[i] == '.' || float_as_str[i - 1] == '.')
			break;
		if (float_as_str[i] == '0')
			float_as_str[i] = 0;
	}
	printf("  value: %s\n", float_as_str);
	fflush(stdout);
	free(float_as_str);
}


/**
 * print_python_bytes - prints information about a Python byte object
 * @p: a PyObject pointer to a Python byte object
 *
*/
void print_python_bytes(PyObject *p)
{
	int i, len;
	char *str, end;

	if (!p || p == Py_None)
		return;
	printf("[.] bytes object info\n");
	fflush(stdout);
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}
	len = PyBytes_Size(p);
	printf("  size: %d\n", len);
	fflush(stdout);
	str = (char *)(void *)((PyBytesObject *)(p))->ob_sval;
	printf("  trying string: %s\n", str);
	fflush(stdout);
	printf("  first %d bytes: ", len > 9 ? 10 : len + 1);
	fflush(stdout);
	for (i = 0; i < 10 && i <= len; i++)
	{
		if (i == 9 || i == len)
			end = '\n';
		else
			end = ' ';
		printf("%.2x%c", str[i], end);
		fflush(stdout);
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

	if (!p || p == Py_None)
		return;
	printf("[*] Python list info\n");
	fflush(stdout);
	if (!PyList_CheckExact(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}
	len = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", len);
	fflush(stdout);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	fflush(stdout);
	for (i = 0; i < len; i++)
	{
		type = PyList_GET_ITEM(p, i)->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		fflush(stdout);
		if (!strncmp(type, "bytes", 5))
			print_python_bytes(PyList_GET_ITEM(p, i));
		if (!strncmp(type, "float", 5))
			print_python_float(PyList_GET_ITEM(p, i));
		fflush(stdout);
	}
}
