#include <stdio.h>
#include <string.h>
#include <zmq.h>
#include "interfaces/messaging_interface.h"

void* context;
void* reply_socket;
void* request_socket;

#define SOCKET_BINDING_ADDRESS "tcp://127.0.0.1:5555"

int initialize_messaging()
{
    int rep_socket_status = 0;

    context = zmq_ctx_new();
    reply_socket = zmq_socket(context, ZMQ_REP);
    rep_socket_status = zmq_bind(reply_socket, SOCKET_BINDING_ADDRESS);

    if (rep_socket_status != 0)
    {
        perror("Error: ZMQ soket binding failed.");
        return -1;
    }

    while(1)
    {
        zmq_msg_t message;
        char* message_data;
        int message_size;

        zmq_msg_init(&message);
        zmq_msg_recv(&message, reply_socket, 0);

        message_data = zmq_msg_data(&message);
        message_size = zmq_msg_size(&message);
        printf("Data: %s, Size: %d\n", message_data, message_size);

        break;
        if (strcmp(message_data, "exit") == 0)
        {
            zmq_msg_close(&message);
            break;
        }
        zmq_msg_close(&message);
    }
    return 0;
}

void free_messaging_resources()
{
    zmq_close(reply_socket);
    zmq_ctx_destroy(context);
}

void send_message(char* message_string)
{
    zmq_msg_t message;
    int message_size = strlen(message_string) + 1;

    zmq_msg_init_size (&message, message_size);
    memcpy(zmq_msg_data(&message), message_string, message_size);

    zmq_msg_send(&message, reply_socket, 0);
}

char* recieve_message()
{
    printf("recieve message\n");
    return NULL;
}
