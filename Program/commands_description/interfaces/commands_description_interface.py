#!/usr/bin/python3
from abc import ABCMeta, abstractmethod


class CommandsDescriptionInterface(metaclass=ABCMeta):

    @abstractmethod
    def execute_command(self, message):
        pass
