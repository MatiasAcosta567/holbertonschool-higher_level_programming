#include "lists.h"

/**
 * create_node - create a new node
 * @number: the n of the struct
 * Return: address of new node
 */

listint_t *create_node(int number)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->next = NULL;
	new->n = number;
	return (new);
}

/**
 * insert_node - insert a node in sorted linked list
 * @head: the head of the linked list
 * @number: the number
 * Return: the address of the node inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux, *new;

	aux = *head;
	new = create_node(number);
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (aux == NULL || aux->n >= number)
	{
		new->next = aux;
		*head = new;
		return (new);
	}

	while (aux && aux->next && aux->next->n < number)
		aux = aux->next;

	new->next = aux->next;
	aux->next = new;

	return (new);
}
