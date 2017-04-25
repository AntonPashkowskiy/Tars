#include "interfaces/messaging_interface.h"

int main()
{
    char* message;

    initialize_messaging();
    free_messaging_resources();

    return 0;
}
