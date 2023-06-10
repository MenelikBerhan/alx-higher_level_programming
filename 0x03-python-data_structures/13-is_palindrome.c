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
	int len = 0;

	if (!head || !(*head) || !(*head)->next)
		return (1);
	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}

	return (is_palindrome_helper(head, len));
}

/**
 * is_palindrome_helper - checks if a list is palindrome
 * @head: pointer to a linked list
 * @len: number of nodes in the list
 *
 * Return: 1 if list is palidrome, or 0 if not.
*/
int is_palindrome_helper(listint_t **head, int len)
{
	listint_t *temp;
	int i, list[1024];

	for (i = 0, temp = *head; i < len; i++, temp = temp->next)
		list[i] = temp->n;

	for (i = 0; i < len / 2; i++)
	{
		if (list[i] != list[len - 1 - i])
		{
			return (0);
		}
	}

	return (1);
}
