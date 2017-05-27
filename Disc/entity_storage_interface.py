#!/usr/bin/python3
from abc import ABCMeta, abstractmethod


class EntityStorageInterface(metaclass=ABCMeta):

    @abstractmethod
    def create(entity):
        pass

    @abstractmethod
    def read(entity_id):
        pass

    @abstractmethod
    def update(entity):
        pass

    @abstractmethod
    def delete(entity_id):
        pass

    @abstractmethod
    def read_all():
        pass
