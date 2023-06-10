#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome_helper - checks the n field value of the first
 *		and last node of a linked list
 * @head: a linked list
 * @len: length of linked list
 *
 * Return: 1 if first and last node n values are equal, or 0 if not
*/
int is_palindrome_helper(listint_t *head, int len)
{
	listint_t *temp;
	int i;

	if (!head || !head->next || len == 1 || len == 0)
		return (1);
	temp = head;
	for (i = 1; i < len; i++)
		temp = temp->next;
	if (head->n != temp->n)
		return (0);
	return (is_palindrome_helper(head->next, len - 2));
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
	int len = 0;

	if (!head || !(*head) || !(*head)->next)
		return (1);
	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}

	return (is_palindrome_helper(*head, len));
}
