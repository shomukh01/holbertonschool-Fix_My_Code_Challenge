#include <stdlib.h>
#include "lists.h"

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *saved_head;
	dlistint_t *target;
	unsigned int position = 0;

	if (head == NULL || *head == NULL)
		return (-1);

	saved_head = *head;
	while (*head != NULL && position < index)
	{
		*head = (*head)->next;
		position++;
	}
	if (*head == NULL)
	{
		*head = saved_head;
		return (-1);
	}

	target = *head;
	if (position == 0)
	{
		*head = target->next;
		if (*head != NULL)
			(*head)->prev = NULL;
	}
	else
	{
		(*head)->prev->next = (*head)->next;
		if ((*head)->next != NULL)
			(*head)->next->prev = (*head)->prev;
		*head = saved_head;
	}

	free(target);
	return (1);
}