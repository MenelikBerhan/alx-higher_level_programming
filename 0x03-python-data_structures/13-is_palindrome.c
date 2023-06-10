#include "lists.h"

/**
 * is_palindrome - checks if a linked list pointed by head is a plindrome
 * @head: a pointer to a linked list
 *
 * Return: 0 if list is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i, len = 0;

	if (!head || !(*head) || !(*head)->next)
		return (1);
	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}

	for (i = 0; i < len / 2; i++)
	{
		if ((*head + (2 * i))->n != (*head + (2 * (len - 1 - i)))->n)
			return (0);
	}
	return (1);
}
