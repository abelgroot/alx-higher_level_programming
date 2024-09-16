#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* list: input list
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if(list == NULL)
		return (0);

	if (fast->next == NULL)
		return (0);
	if (fast == fast->next)
		return (1);
	if (fast == (fast->next)->next)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
