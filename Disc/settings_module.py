#!/usr/bin/python3
from common import constants
from common.utils.singleton import Singleton

class SettingsModule(metaclass=Singleton):
    def __init__(self):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def get_all_settings(self):
        pass

    def get_settings_by_keys(self, keys_list):
        pass

    def export_settings(self, destination_path):
        pass

    def import_settings(self, source_path):
        pass