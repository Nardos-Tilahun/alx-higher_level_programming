#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check the code
 * @list: list of linked lists
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *once, *twice;

	if (list == NULL)
		return (0);
	once = list;
	twice = list->next;
	while (twice && twice->next != NULL)
	{
		if (once == twice)
			return (1);
		once = once->next;
		twice = twice->next->next;
	}
	return (0);
}
