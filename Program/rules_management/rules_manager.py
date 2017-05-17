#!/usr/bin/python3
from common.utils.singleton import Singleton


class RulesManager(metaclass=Singleton):
    def __init__(self):
        self._add_directory_callback = None
        self._remove_directory_callback = None

    def create_rule(self, rule):
        pass

    def update_rule(self, rule):
        pass

    def delete_rule(self, rule_id):
        pass

    def read_all_rules(self):
        pass

    def get_rules(self, event_info, analyze_results=None):
        pass

    def export_rules(self, target_file):
        pass

    def import_rules(self, source_file):
        pass

    def add_directory_list_change_handlers(self, add_callback, remove_callback):
        self._add_directory_callback = add_callback
        self._remove_directory_callback = remove_callback