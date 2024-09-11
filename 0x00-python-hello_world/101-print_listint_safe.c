#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* print_listint_safe - Prints a listint_t linked list safely (handles loops).
* @head: Pointer to the head of the list.
*
* Return: The number of nodes in the list.
*/
size_t print_listint_safe(const listint_t *head)
{
	const listint_t *slow = head;
	const listint_t *fast = head;
	size_t count = 0;
	int loop_detected = 0;

	if (head == NULL)
	{
		printf("%d\n", 0);
		exit(98);
	}
	if (fast == fast->next)
	{
		printf("[%p] %d\n", (void *)fast, fast->n);
		printf("-> [%p] %d\n", (void *)fast, fast->n);
		return (1);
	}
	if (fast == (fast->next)->next)
	{
		printf("[%p] %d\n", (void *)fast, fast->n);
		printf("[%p] %d\n", (void *)fast->next, (fast->next)->n);
		printf("-> [%p] %d\n", (void *)fast, fast->n);
		return (2);
	}
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			loop_detected = 1;
			break;
		}
	}
	count = print_loop(head, fast, loop_detected);
	return (count);
}

/**
* print_loop - print the loops iteratively supportive func.
*	@head: the list head.
*	@fast: next fast list pointer.
*	@loop_detected: 1 if loop detected, 0 otherwise.
*
*	Return: the count of the nodes.
*/
size_t print_loop(const listint_t *head,
	const listint_t *fast, int loop_detected)
{
	const listint_t *slow = head, *node = head;
	const listint_t *loop_start = NULL, *loop_node = NULL;
	size_t count = 0;

	if (loop_detected)
	{
		while (slow != fast)
		{
			slow = slow->next;
			fast = fast->next;
		}
		loop_start = slow;
		while (node != loop_start)
		{
			printf("[%p] %d\n", (void *)node, node->n);
			node = node->next;
			count++;
		}
		printf("[%p] %d\n", (void *)loop_start, loop_start->n);
		count++;
		loop_node = loop_start->next;
		while (loop_node != loop_start)
		{
			printf("[%p] %d\n", (void *)loop_node, loop_node->n);
			loop_node = loop_node->next;
			count++;
		}
		printf("-> [%p] %d\n", (void *)loop_start, loop_start->n);
	}
	else
	{
		node = head;
		while (node != NULL)
		{
			printf("[%p] %d\n", (void *)node, node->n);
			node = node->next;
			count++;
		}
	}
	return (count);
}
