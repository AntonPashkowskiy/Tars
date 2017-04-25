#include <string.h>
#include <stdlib.h>
#include "monitor_action.h"

#define MESSAGE_PARTS_DELIMETER ":"

struct monitor_action parse_message(char* message)
{
    struct monitor_action action;
    char* message_part;

    message_part = strtoc(message, MESSAGE_PARTS_DELIMETER);
    action.id = message_part == NULL ? 0 : atoi(message_part);

    message_part = strtoc(NULL, MESSAGE_PARTS_DELIMETER);
    action.target = message_part;

    message_part = strtoc(NULL, MESSAGE_PARTS_DELIMETER);
    action.modificators = message_part == NULL ? 0 : atoi(message_part);

    return action;
}

char* get_message(struct monitor_action action)
{
    char* message;
    char id_part[20], modificators_part[20];
    int message_length;

    itoa(action.id, id_part, 10);
    itoa(action.modificators, modificators_part, 10);

    message_length = strlen(id_part) + strlen(action.target) + strlen(modificators_part);
    message = (char*)malloc(message_length * sizeof(char));
    message[0] = '\0';

    strcat(message, id_part);
    strcat(message, MESSAGE_PARTS_DELIMETER);
    strcat(message, action.target);
    strcat(message, MESSAGE_PARTS_DELIMETER);
    strcat(message, modificators_part);
}
