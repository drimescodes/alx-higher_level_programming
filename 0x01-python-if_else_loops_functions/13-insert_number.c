#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		while (current != NULL && current->n < number)
		{
			prev = current;
			current = current->next;
		}
		if (current == *head)
		{
			new->next = *head;
			*head = new;
		}
		else
		{
			new->next = current;
			prev->next = new;
		}
	}
	return (new);
}
