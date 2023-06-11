#include <Python.h>
/**
 * struct dict_s - singly linked list mapping PyOject address with
 * 		alloc'ed memory size
 * @alloc_ed: size of memory allocated
 * @address: address of a PyObject
 * @next: pointer to next node in the list
*/
typedef struct dict_s
{
	int alloc_ed;
	PyObject *address;
	struct dict_s *next;
} dict_t;

/**
 * add_node - adds a new node at the start of a list pointed by head
 *		or updates a nodes alloc_ed field if it already exists
 * @head: pointer to a linked list
 * @p: address of a PyObject
 * @alloc_ed: memory alloc'ed
 * @update: boolean value of 0 if the node already exists, or 1 if not
*/
void add_node(dict_t **head, PyObject *p, int alloc_ed, int update)
{
	dict_t *new, *temp;

	if (!update)
	{
		new = malloc(sizeof(dict_t));
		new->alloc_ed = alloc_ed;
		new->address = p;
		new->next = *head;
		*head = new;
	}
	else
	{
		temp = *head;
		while (temp)
		{
			if (temp->address == p)
				break;
			temp = temp->next;
		}
		temp->alloc_ed = alloc_ed;
	}

}

/**
 * find_object - checks if a node exists in a list
 * @head: a linked list
 * @p: a PyObject address
 *
 * Return: the alloc_ed field of the node if found, or -1 if not found.
*/
int find_object(dict_t *head, PyObject *p)
{
	while (head)
	{
		if (head->address == p)
			return (head->alloc_ed);
		head = head->next;
	}
	return (-1);
}

/**
 * print_python_list_info - prints information about a Python list
 * @p: a PyObject pointer to the list
 *
*/
void print_python_list_info(PyObject *p)
{
	int i, len, alloc_ed, update = 0;
	static dict_t *head;

	if (!p || p == Py_None || !PyList_Check(p))
		exit(0);

	len = PyList_Size(p);
	alloc_ed = find_object(head, p);
	if (alloc_ed == -1)
		alloc_ed = len;
	else if (len > alloc_ed)
	{
		alloc_ed  = len + (len >> 3) + (len < 9 ? 3 : 6);
		update = 1;
	}
	add_node(&head, p, alloc_ed, update);
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", alloc_ed);

	for (i = 0; i < len; i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);

}
