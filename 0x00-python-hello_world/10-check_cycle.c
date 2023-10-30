#include "lists.h"
/**
 * check_cycle - Checks if a singly lined list has a cycle in it
 * @list: the list to check into
 * Return: 0 if there is no cycle, and 1 otherwise
 */
int check_cycle(listint_t *list)
{
	struct listint_s *current, *temp;

	if (!list || !list->next)
		return (0);

	current = list;
	temp = list;

	while (current)
	{
		current = current->next;
		if (current == temp)
			return (1);
	}

	return (0);
}
