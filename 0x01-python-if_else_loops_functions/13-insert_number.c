#include "lists.h"

listint_t *add_node_start(int number)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->next = NULL;
	new->n = number;
	return (new);
}


listint_t *add_node(listint_t *node, int number)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->next = node->next;
	node->next = new;
}

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux;
	int position = 0;

	aux = *head;
	if (aux == NULL)
		return (add_node_start(number));
	while (aux->n < number)
	{
		aux = aux->next;
		position++;
	}
	if (aux->next == NULL)
	{
		return(add_node_end(aux, number));
	}
	else
	{
		return(add_node(aux, number));
	}
}
