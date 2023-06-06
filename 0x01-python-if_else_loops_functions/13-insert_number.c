#include "lists.h"

/**
 * insert_node - adds a new node in a sorted linked list
 * @head: a pointer to a sorted linked list
 * @number: n field value of the new node
 *
 * Return: a pointer to the new node or NULL for failure
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp, *current;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!(*head))
	{
		new_node->next = NULL;
		*head = new_node;
	}
	else
	{
		temp = current = *head;
		while (current)
		{
			if (current->n > number)
			{
				new_node->next = current;
				if (temp != current)
					temp->next = new_node;
				else
					*head = new_node;
				break;
			}
			else if (current->next == NULL)
			{
				new_node->next = NULL;
				current->next = new_node;
				break;
			}
			temp = current;
			current = current->next;
		}
	}
	return (new_node);
}
