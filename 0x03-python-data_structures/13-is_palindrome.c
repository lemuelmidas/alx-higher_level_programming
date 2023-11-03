#include "lists.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
  * is_palindrome - This checks if a list is a palindrome.
  * @head: The pointer to the head of the list.
  * Return: 0 if list not a palindrome, else 1.
  */
int is_palindrome(listint_t **head)
{
	listint_t *mem = *head;
	int nodes = 0, i = 0, *array = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (mem)
	{
		nodes++;
		mem = mem->next;
	}
	array = malloc(sizeof(int) * nodes);
	mem = *head;
	while (mem)
	{
		array[i++] = mem->n;
		mem = mem->next;
	}
	for (i = 0; i < nodes / 2; i++)
	{
		if (array[i] != array[nodes - 1 - i])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
