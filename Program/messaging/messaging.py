#!/usr/bin/python3
from interfaces.messaging_interface import MessagingInterface
import zmq

def get_socket_binding_address():
    return "tcp://127.0.0.1:5555";

class MessagingManager(MessagingInterface):
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(get_socket_binding_address())
        pass

    def __del__(self):
        self.socket.close();
        self.context.destroy();


    def send_message(self, message):
        self.socket.send_unicode(message)


    def recieve_message(self):
        print("recieve message")
        return None
