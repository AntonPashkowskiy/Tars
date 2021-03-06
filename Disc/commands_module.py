#!/usr/bin/python3
from commands_description.interfaces.commands_description_interface import CommandsDescriptionInterface
from common.commands_description import target_block_types, action_types
from common.settings import setting_keys
from settings.settings_module import SettingsModule
from logger.logger_module import LoggerModule
from rules_management.rules_manager import RulesManager
from monitor_interaction.monitor_interaction_manager import MonitorInteractionManager


class CommandsDescriptionModule(CommandsDescriptionInterface):
    def __init__(self):
        self._commands_handler_table = {
            # commands to settings block
            (target_block_types.SETTINGS_BLOCK, action_types.CREATE): self._create_setting_handler,
            (target_block_types.SETTINGS_BLOCK, action_types.READ): self._read_settings_handler,
            (target_block_types.SETTINGS_BLOCK, action_types.UPDATE): self._update_setting_handler,
            (target_block_types.SETTINGS_BLOCK, action_types.DELETE): self._delete_setting_handler,
            (target_block_types.SETTINGS_BLOCK, action_types.IMPORT): self._import_settings_handler,
            (target_block_types.SETTINGS_BLOCK, action_types.EXPORT): self._export_settings_handler,

            # commands to event log block
            (target_block_types.EVENT_LOG_BLOCK, action_types.READ): self._read_event_log_handler,
            (target_block_types.EVENT_LOG_BLOCK, action_types.RESTORE): self._restore_state_by_event_log_handler,

            # commands to rules management block
            (target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.CREATE): self._create_rule_handler,
            (target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.READ): self._read_rules_handler,
            (target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.UPDATE): self._update_rule_handler,
            (target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.DELETE): self._delete_rule_handler,
            (target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.IMPORT): self._import_rules_handler,
            (target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.EXPORT): self._export_rules_handler,

            # commands to monitor interaction block
            (target_block_types.MONITOR_INTERACTION_BLOCK, action_types.EXECUTE): self._execute_action_handler,
            (target_block_types.MONITOR_INTERACTION_BLOCK, action_types.START): self._start_monitor_handler,
            (target_block_types.MONITOR_INTERACTION_BLOCK, action_types.STOP): self._stop_monitor_handler
        }
        #self._settings_module = SettingsModule()
        #self._logger_module = LoggerModule(self.settings_module[setting_keys.LOG_FILE_NAME], None)
        #self._rules_manager = RulesManager()
        #self._monitor_interaction_manager = MonitorInteractionManager()

    def execute_command(self, command):
        if command is None:
            raise ValueError("Command object is None.")
        command_handler = self._commands_handler_table.get((command.target_block, command.action))

        if command_handler is None:
            raise NotImplementedError("Handler for passed command is not exist")
        return command_handler(command.additional_information)

    def _create_setting_handler(self, setting):
        #key, value = setting
        #self._settings_module[key] = value
        pass

    def _read_settings_handler(self, parameters):
        #if parameters is None:
        #    return self._settings_module.get_all_settings()
        #elif isinstance(parameters, str):
        #    return self._settings_module[parameters]
        #elif isinstance(parameter, list):
        #    return self._settings_module.get_settings_by_keys(parameters)
        return ("test", "test")

    def _update_setting_handler(self, setting):
        #key, value = setting
        #self._settings_module[key] = value
        pass

    def _delete_setting_handler(self, key):
        #del self._settings_module[key]
        pass

    def _import_settings_handler(self, import_parameters):
        #self._settings_module.import_settings(import_parameters)
        pass

    def _export_settings_handler(self, export_parameters):
        #self._settings_module.export_settings(export_parameters)
        pass

    def _read_event_log_handler(self, parameters):
        #start_date, end_date = parameters
        #self._logger_module.read_events_info_daterange(start_date, end_date)
        pass

    def _restore_state_by_event_log_handler(self, parameters):
        #if isinstance(parameters, int):
        #    log_record = self._logger_module.read_event_info(parameters)
            #restoring code
        #elif isinstance(param, tuple):
        #    start_record_id, end_record_id = parameters
        #    log_records = self._logger_module.read_events_info_range(start_record_id, end_record_id)
            #restoring code
        pass

    def _create_rule_handler(self, rule):
        #self._rules_manager.create_rule(rule)
        pass

    def _read_rules_handler(self, parameters):
        #return self._rules_manager.read_all_rules()
        pass

    def _update_rule_handler(self, rule):
        #self._rules_manager.update_rule(rule)
        pass

    def _delete_rule_handler(self, rule_id):
        #self._rules_manager.delete_rule(rule_id)
        pass

    def _import_rules_handler(self, source_file):
        #self._rules_manager.import_rules(source_file)
        pass

    def _export_rules_handler(self, target_file):
        #self._rules_manager.export_rules(target_file)
        pass

    def _execute_action_handler(self, parameters):
        #target_file_path, action = parameters
        #self._monitor_interaction_manager.execute_action_immediately(target_file_path, action)
        pass

    def _start_monitor_handler(self, parameters):
        #self._monitor_interaction_manager.start_monitor()
        pass

    def _stop_monitor_handler(self, parameters):
        #self._monitor_interaction_manager.stop_monitor()
        pass
