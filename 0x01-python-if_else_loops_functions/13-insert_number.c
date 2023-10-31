#include "lists.h"

/**
 * insert_node - insert node in order
 * @head: head of the linked list
 * @number: number that will be inserted
 * Return: return the new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *move, *ptr;

	if (!head)
		return (NULL);
	ptr = malloc(sizeof(listint_t));
	if (!ptr)
		return (NULL);
	ptr->n = number;
	if (*head == NULL)
	{
		*head = ptr;
		ptr->next = NULL;
		return (*head);
	}
	move = *head;
	if (number < move->n)
	{
		ptr->n = number;
		ptr->next = move;
		*head = ptr;
		return (*head);
	}
	while (move->next != NULL && move->next->n < number)
		move = move->next;
	if (move->next == NULL)
	{
		move->next = ptr;
		ptr->next = NULL;
	}
	else
	{
		ptr->next = move->next;
		move->next = ptr;
	}
	return (*head);
}
