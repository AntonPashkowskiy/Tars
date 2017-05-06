#!/usr/bin/python3
#from commands_description.interfaces.commands_description_interface import CommandsDescriptionInterface
from common.commands_description import target_block_types, action_types


class CommandsDescriptionModule:
    def __init__(self):
        self._commands_handler_table = {
            # commands to settings block
            (target_block_types.SETTINGS_BLOCK, action_types.CREATE): _create_setting_handler,
            (target_block_types.SETTINGS_BLOCK, action_types.READ): _read_settings_handler,
            (target_block_types.SETTINGS_BLOCK, action_types.UPDATE): _update_setting_handler,
            (target_block_types.SETTINGS_BLOCK, action_types.DELETE): _delete_setting_handler,
            (target_block_types.SETTINGS_BLOCK, action_types.IMPORT): _import_settings_handler,
            (target_block_types.SETTINGS_BLOCK, action_types.EXPORT): _export_settings_handler,

            # commands to event log block
            (target_block_types.EVENT_LOG_BLOCK, action_types.READ): _read_event_log_handler,
            (target_block_types.EVENT_LOG_BLOCK, action_types.RESTORE): _restore_state_by_event_log_handler,

            # commands to rules management block
            (target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.CREATE): _create_rule_handler,
            (target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.READ): _read_rules_handler,
            (target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.UPDATE): _update_rule_handler,
            (target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.DELETE): _delete_rule_handler,
            (target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.IMPORT): _import_rules_handler,
            (target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.EXPORT): _export_rules_handler,

            # commands to monitor interaction block
            (target_block_types.MONITOR_INTERACTION_BLOCK, action_types.EXECUTE): _execute_action_handler,
            (target_block_types.MONITOR_INTERACTION_BLOCK, action_types.START): _start_monitor_handler,
            (target_block_types.MONITOR_INTERACTION_BLOCK, action_types.STOP): _stop_monitor_handler
        }

    def execute_command(self, command):
        pass

    def _create_setting_handler(self, setting):
        pass

    def _read_settings_handler(self, parameters):
        pass

    def _update_setting_handler(self, setting):
        pass

    def _delete_setting_handler(self, setting):
        pass

    def _import_settings_handler(self, import_parameters):
        pass

    def _export_settings_handler(self, export_parameters):
        pass

    def _read_event_log_handler(self, parameters):
        pass

    def _restore_state_by_event_log_handler(self, parameters):
        pass

    def _create_rule_handler(self, rule):
        pass

    def _read_rules_handler(self, parameters):
        pass

    def _update_rule_handler(self, rule):
        pass

    def _delete_rule_handler(self, rule):
        pass

    def _import_rules_handler(self, parameters):
        pass

    def _export_rules_handler(self, parameters):
        pass

    def _execute_action_handler(self, parameters):
        pass

    def _start_monitor_handler(self, parameters):
        pass

    def _stop_monitor_handler(self, parameters):
        pass


if __name__ == "__main__":
    pass