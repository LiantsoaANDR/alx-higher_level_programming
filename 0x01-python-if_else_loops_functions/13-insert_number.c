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
	unsigned int i = 0;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	current = *head;
	new->n = number;

	while (current && number < current->next->n)
	{
		before = current;
		current = current->next;
		i++;
	}

	before->next = new;
	new->next = current;

	return (new);
}
