#!/usr/bin/python3
from messaging_manager import MessagingManager, MessagingManagerType
from time import sleep


def main():
    server = MessagingManager(MessagingManagerType.SERVER, "tcp://127.0.0.1:5555")
    client = MessagingManager(MessagingManagerType.CLIENT, "tcp://127.0.0.1:5555")
    
    client.send_message("message 1")
    client.send_message("message 2")
    client.send_message("message 3")
    client.send_message("message 4")
    server.send_message("message 5")
    server.send_message("message 6")
    server.send_message("exit")

    sleep(2)

    print("Messages from client")
    print(server.recieve_message() or "lol 1")
    print(server.recieve_message() or "lol 1")
    print(server.recieve_message() or "lol 1")
    print(server.recieve_message() or "lol 1")

    print("Messsages from server")
    print(client.recieve_message() or "lol 2")
    print(client.recieve_message() or "lol 2")
    print(client.recieve_message() or "lol 2")


if __name__ == "__main__":
    main()
