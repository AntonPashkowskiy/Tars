
struct linked_list
{
    void* data_pointer;
    struct linked_list* next_element;
}

linked_list* add_element_to_list(struct linked_list* list, void* element);
int get_list_lenght(struct linked_list* list);
void* get_list_data_by_index(struct linked_list* list, int index);
