#include <stdlib.h>
#include "linked_list.h"

struct linked_list* linked_list_add_data(struct linked_list* list_top, void* data, int is_dynamic_memory) 
{
    struct linked_list new_element;

    new_element.data_pointer = data;
    new_element.is_dynamic_memory = is_dynamic_memory;
    new_element.previous_element = NULL;
    new_element.next_element = NULL;
    new_element.last_element = NULL;

    if (list_top == NULL) 
    {
        list_top = &new_element;
    }
    else if (list_top != NULL && (list_top -> next_element) == NULL)
    {
        new_element.previous_element = list_top;
        list_top -> next_element = &new_element;
        list_top -> last_element = &new_element;
    }
    else 
    {
        new_element.previous_element = list_top -> last_element;
        list_top -> last_element -> next_element = &new_element;
        list_top -> last_element = &new_element;
    }
    return list_top;
}

int linked_list_length(struct linked_list* list_top)
{
    int length = 0;
    struct linked_list* current_list_element = list_top;

    while (current_list_element != NULL) 
    {
        length ++;
        current_list_element = current_list_element -> next_element;
    }
    return length;
}

void* linked_list_get_by_index(struct linked_list* list_top, int index)
{
    int current_index = 0;
    struct linked_list* current_list_element = list_top;

    while (current_list_element != NULL)
    {
        if (current_index == index)
        {
            return current_list_element -> data_pointer;
        }
        current_index ++;
        current_list_element = current_list_element -> next_element;
    }
    return NULL;
}

void linked_list_free(struct linked_list* list_top)
{
    struct linked_list* current_list_element = list_top;

    while (current_list_element != NULL)
    {
        if (current_list_element -> is_dynamic_memory) 
        {
            free(current_list_element -> data_pointer);
        }
        current_list_element = current_list_element -> next_element;
    }
    list_top = NULL;
}