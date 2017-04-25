
struct monitor_action
{
    int id;
    char* target;
    int modificators;
};

struct monitor_action parse_message(char* message);
char* get_message(struct monitor_action action);
