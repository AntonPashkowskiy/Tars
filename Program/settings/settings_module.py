from common import constants
from common.utils.singleton import Singleton

class SettingsModule(metaclass=Singleton):
    def __init__(self):
        pass

    def __getitem__(self, key):
        pass

    def export_settings(self, destination_path):
        pass

    def import_settings(self, source_path):
        pass