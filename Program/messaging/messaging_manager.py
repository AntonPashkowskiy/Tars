#!/usr/bin/python3
from messaging.interfaces.messaging_interface import MessagingInterface
from enum import Enum
from queue import Queue
from threading import Thread, Event
import zmq


def bind_socket_to_address(socket, messaging_manager_type, binding_address):
    if messaging_manager_type == MessagingManagerType.CLIENT:
        socket.connect(binding_address)
    elif messaging_manager_type == MessagingManagerType.SERVER:
        socket.bind(binding_address)


class MessagingManagerType(Enum):
    CLIENT = 1
    SERVER = 2


class MessagingManagerBackgroudReciever(Thread):
    def __init__(self, messaging_manager_type, socket_binding_address, queues, events):
        super().__init__()
        send_queue, recieve_queue = queues
        stop_event, message_ready_event = events

        self._send_queue = send_queue
        self._recieve_queue = recieve_queue
        self._stop_event = stop_event
        self._message_ready_event = message_ready_event
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.PAIR)

        bind_socket_to_address(self._socket, messaging_manager_type, socket_binding_address)

    def run(self):
        polling_delay = 100

        while not self._stop_event.is_set():
            if self._send_queue.qsize() != 0:
                self._socket.send_unicode(self._send_queue.get())
            events = self._socket.poll(polling_delay)
            if events != 0:
                self._recieve_queue.put(self._socket.recv(flags=zmq.NOBLOCK))
                if self._message_ready_event is not None:
                    self._message_ready_event.set()
        self._socket.close()
        self._context.destroy()


class MessagingManager(MessagingInterface):
    def __init__(self, messaging_manager_type, socket_binding_address, message_ready_event=None):
        self._send_queue = Queue()
        self._recieve_queue = Queue()
        self._background_worker_stop_event = Event()
        self._background_worker = MessagingManagerBackgroudReciever(messaging_manager_type, \
            socket_binding_address, \
            (self._send_queue, self._recieve_queue), \
            (self._background_worker_stop_event, message_ready_event))
        self._background_worker.start()

    def __del__(self):
        self._background_worker_stop_event.set()

    def send_message(self, message):
        self._send_queue.put(message)

    def recieve_message(self):
        if self._recieve_queue.qsize() != 0:
            return self._recieve_queue.get().decode("utf-8")
        return None

    def get_all_recieved_messages(self):
        return []
