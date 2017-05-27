#!/usr/bin/python3
from storage.interfaces.entity_storage_interface import EntityStorageInterface


class EntityStorage(EntityStorageInterface):
    def __init__(self, target_collection):
        self._target_collection = target_collection

    def create(entity):
        pass

    def read(entity_id):
        pass

    def update(entity):
        pass

    def delete(entity_id):
        pass

    def read_all():
        pass