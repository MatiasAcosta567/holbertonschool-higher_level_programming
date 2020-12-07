#include "lists.h"

/**
 * check_cycle - check if a linked list have a cicle
 * list: the head of a list
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
