#include "lists.h"
#include <stdlib.h>
#include <string.h>
/**
 * add_node - adds a new node at the beginning of a listint_t list
 * @head: pointer to the pointer head
 * @n: the int to be included in the new node
 * Return: the address of the new element, or NULL if it failed
 */
listint_t *add_node(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (0);

	new->n = n;
	new->next = *head;
	*head = new;

	return (*head);
}
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: pointer to the pointer of the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *reversed, *reversed_current;

	if (!head || !(*head))
		return (1);

	current = *head;
	while (current)
	{
		add_node(&reversed, current->n);
		current = current->next;
	}

	current = *head;
	reversed_current = reversed;
	while (current)
	{
		if (current->n != reversed_current->n)
		{
			free_listint(reversed);
			return (0);
		}
		current = current->next;
		reversed_current = reversed_current->next;
	}

	free_listint(reversed);
	return (1);
}
