#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a linked list pointed by head is a plindrome
 * @head: a pointer to a linked list
 *
 * Return: 0 if list is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i, len = 0, *list;

	if (!head || !(*head))
		return (1);
	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	list = malloc(sizeof(int) * len);
	if (!list)
	{
		perror("malloc failure");
		exit(98);
	}
	for (i = 0, temp = *head; i < len; i++, temp = temp->next)
		list[i] = temp->n;

	for (i = 0; i < len / 2; i++)
	{
		if (list[i] != list[len - 1 - i])
		{
			free(list);
			return (0);
		}
	}
	free(list);

	return (1);
}
