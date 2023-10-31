#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the pointer of the head of the list
 * @number: the number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *before;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;

	if (!head)
		return (NULL);

	if (!(*head))
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	current = *head;

	while (current && current->next)
	{
		if (current->next->n > number)
		{
			before = current;
			current = current->next;
			break;
		}
		current = current->next;
	}

	before->next = new;
	new->next = current;

	return (new);
}
