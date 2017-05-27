#!/usr/bin/python3
from abc import ABCMeta, abstractmethod


class MessagingInterface(metaclass=ABCMeta):

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def recieve_message(self):
        pass
