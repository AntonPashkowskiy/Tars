#!/usr/bin/python3
from common.utils.singleton import Singleton


class RulesManager(metaclass=Singelton):
    def __init__(self):
        pass

    def create_rule(self, rule):
        pass

    def update_rule(self, rule):
        pass

    def delete_rule(self, rule_id):
        pass

    def read_all_rules(self, rule):
        pass

    def get_rules(self, event_info, analyze_results=None):
        pass

    def export_rules(self, target_file):
        pass

    def import_rules(self, source_file):
        pass