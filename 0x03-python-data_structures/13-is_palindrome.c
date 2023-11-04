#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
int reversecheck(listint_t **head, listint_t **head2, int len);
/**
 * is_palindrome - Check the palindrom
 * @head: accept the head of the linked lists
 *
 * Return: return the status
 */
int is_palindrome(listint_t **head)
{
	listint_t *move;
	int i, check, len, len1;

	if (!head || !(*head) || !((*head)->next))
		return (1);
	move = *head;
	for (i = 0; move; i++)
		move = move->next;
	if (i % 2 == 0)
		len1 = i / 2;
	else
		len1 = i / 2 + 1;
	len = i / 2;
	move = *head;
	for (i = 0; i < len1; i++)
		move = move->next;
	check = reversecheck(head, &move, len);
	return (check);
}
/**
 * reversecheck - Check the palindrom
 * @head: accept the head of the linked lists
 * @head2: accept the head of the second half linked list
 * @len: the length of iteration
 *
 * Return: return the status
 */
int reversecheck(listint_t **head, listint_t **head2, int len)
{
	listint_t *temp, *temp1, *temp2, *move, *move1;
	int i;

	if (!head || !(*head) || !((*head)->next))
		return (1);
	if (!head2 || !(*head2))
		return (1);
	move = *head2;
	temp1 = NULL;
	while (move && move->next)
	{
		temp2 = move->next->next;
		move->next->next = move;
		temp = move->next;
		move->next = temp1;
		temp1 = temp;
		move = temp2;
	}
	if ((move && !(move->next)) && len % 2)
		move->next = temp1;
	else
		move = temp1;
	move1 = *head;
	for (i = 0; i < len; i++)
	{
		if (move->n == move1->n)
		{
			move = move->next;
			move1 = move1->next;
		}
		else
			break;
	}
	if (i == len)
		return (1);
	return (0);
}
