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
        all_suitable_rules = self._get_all_suitable_rules(event_info, analyze_results)
        
        if self._is_ignore_rule_exist(all_suitable_rules):
            return []
        
        specific_sorted_rules = self._sort_by_specific_level(all_suitable_rules)
        top_specific_rules = self._get_top_specific_rules(specific_sorted_rules)
        delete_rules = self._get_rules_by_action_type(top_specific_rules, action_types.DELETE_FILE)
        
        if len(delete_rules) != 0:
            return [ delete_rules[0] ]
        return self._get_final_rules_sequence(specific_sorted_rules)

    def export_rules(self, target_file):
        pass

    def import_rules(self, source_file):
        pass

    def add_directory_list_change_handlers(self, add_callback, remove_callback):
        self._add_directory_callback = add_callback
        self._remove_directory_callback = remove_callback