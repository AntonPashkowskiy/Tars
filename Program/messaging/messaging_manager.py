#!/usr/bin/python3
from interfaces.messaging_interface import MessagingInterface
from enum import Enum
from queue import Queue
from threading import Thread, Event
import zmq


def get_socket_binding_address():
    return "tcp://127.0.0.1:5555";


def bind_socket_to_address(socket, messaging_manager_type, binding_address):
    if messaging_manager_type == MessagingManagerType.CLIENT:
        socket.connect(binding_address)
    elif messaging_manager_type == MessagingManagerType.SERVER:
        socket.bind(binding_address)


class MessagingManagerType(Enum):
    CLIENT = 1
    SERVER = 2


class MessagingManagerBackgroudReciever(Thread):
    def __init__(self, messaging_manager_type, send_queue, recieve_queue, stop_event):
        Thread.__init__(self)
        self.send_queue = send_queue
        self.recieve_queue = recieve_queue
        self.stop_event = stop_event
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)

        bind_socket_to_address(self.socket, messaging_manager_type, get_socket_binding_address())

    def run(self):
        polling_delay = 100

        while not self.stop_event.is_set():
            if self.send_queue.qsize() != 0:
                self.socket.send_unicode(self.send_queue.get())
            events = self.socket.poll(polling_delay)
            if events != 0:
                self.recieve_queue.put(self.socket.recv(flags=zmq.NOBLOCK))
        self.socket.close()
        self.context.destroy()


class MessagingManager(MessagingInterface):
    def __init__(self, messaging_manager_type):
        self.send_queue = Queue()
        self.recieve_queue = Queue()
        self.background_worker_stop_event = Event()
        self.background_worker = MessagingManagerBackgroudReciever(messaging_manager_type, self.send_queue, self.recieve_queue, self.background_worker_stop_event)
        self.background_worker.start()

    def __del__(self):
        self.background_worker_stop_event.set()

    def send_message(self, message):
        self.send_queue.put(message)

    def recieve_message(self):
        if self.recieve_queue.qsize() != 0:
            return self.recieve_queue.get().decode("utf-8")
        return None
