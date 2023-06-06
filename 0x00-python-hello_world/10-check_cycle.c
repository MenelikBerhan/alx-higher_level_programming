#include "lists.h"

/**
 * check_cycle - checks if a list has a loop or not.
 * @list: a listint_t type linked list.
 *
 * Return: 1 if loop is found or 0 if not.
*/
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	if (!list)
		return (0);
	hare = tortoise = list;
	while ((tortoise = tortoise->next) && (hare = hare->next)
				&& (hare = hare->next))
		if (tortoise == hare)
			return (1);

	return (0);
}
