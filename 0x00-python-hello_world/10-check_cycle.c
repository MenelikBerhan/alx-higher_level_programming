#include "lists.h"

/**
 * check_cycle - checks if a list has a loop or not.
 * @list: a listint_t type linked list.
 *
 * Return: 1 if loop is found or 0 if not.
*/
int check_cycle(listint_t *list)
{
	listint_t *temp, *start;

	if (!list)
		return (0);

	start = list;
	while (list)
	{
		temp = start;
		while (1)
		{
			if (list->next == temp)
				return (1);
			if (temp == list)
				break;
			temp = temp->next;
		}
		list = list->next;
	}
	return (0);
}
