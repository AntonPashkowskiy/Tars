#include <stdio.h>
#include <sdtlib.h>
#include <string.h>
#include "utils/linked_list.c"

int main() 
{
    printf("# LINKED LIST TESTS\n");

    struct linked_list* list_top;
    int integer_data = 23;
    char* const_string_data = "Static string test.";
    char* dynamic_string_data = (char*)malloc(10 * sizeof(char));
    strcpy(dynamic_string_data, "Dynamic string test.");

    printf("# Linked list test. Adding elements.\n\n");

    list_top = linked_list_add_data(list_top, &integer_data, 0);
    list_top = linked_list_add_data(list_top, const_string_data, 0);
    list_top = linked_list_add_data(list_top, dynamic_string_data, 1);

    printf("# Linked list test. List length.\n\n");

    printf("List length is %d.\n\n", linked_list_length(list_top));

    printf("# Linked list test. Get element data by index.\n\n");

    printf("Third element: %s.\n", (char*)linked_list_get_by_index(list_top, 2));
    printf("Second element: %s.\n", (char*)linked_list_get_by_index(list_top, 1));
    printf("First element: %s.\n\n", *((int*)linked_list_get_by_index(list_top, 0)));
    
    printf("# Linked list test. Free list.\n\n");

    linked_list_free(list_top);

    return 0;
}
