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
	int check = 0;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	if (!head)
		return (NULL);

	new->n = number;
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
			break;
		current = current->next;
		check = 1;
	}

	before = current;
	current = current->next;
	if (check)
	{
		before->next = new;
		new->next = current;
	}
	if (!check)
		new->next = before;

	return (new);
}
