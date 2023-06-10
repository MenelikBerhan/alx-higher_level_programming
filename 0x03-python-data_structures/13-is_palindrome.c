#include "lists.h"
#include <stdio.h>


/**
 * get_element - finds the element at index index in a linked list list
 * @head: a linked list
 * @index: index of node to be found
 *
 * Return: a pointer to the node at index
*/
listint_t *get_element(listint_t *head, int index)
{
	int i;

	for (i = 0; i < index; i++)
		head = head->next;
	return (head);
}

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

	if (!head || !(*head))
		return (1);
	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}

	for (i = 0, temp = *head; i < len / 2; i++, temp = temp->next)
		if (temp->n != (get_element(*head, len - 1 - i))->n)
			return (0);

	return (1);
}
