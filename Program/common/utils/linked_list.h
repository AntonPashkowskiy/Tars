
struct linked_list
{
    void* data_pointer;
    int is_dynamic_memory;
    
    struct linked_list* previous_element;
    struct linked_list* next_element;
    struct linked_list* last_element;
};

struct linked_list*     linked_list_add_data(struct linked_list* list_top, void* data, int is_dynamic_memory);
int                     linked_list_length(struct linked_list* list_top);
void*                   linked_list_get_by_index(struct linked_list* list_top, int index);
void                    linked_list_free(struct linked_list* list_top);