#!/usr/bin/python3
from common.rules_management.actions import rule_actions_types


class RuleAction:
    def __init__(self, action_type):
        self._action_type = action_type

    @property
    def action_type(self):
        return self._action_type


class DeleteFileRuleAction(RuleAction):
    def __init__(self, is_permanent_deleting):
        super().__init__(rule_actions_types.DELETE_FILE)
        self._is_permanent_deleting = is_permanent_deleting

    @property
    def is_permanent_deleting(self):
        return self._is_permanent_deleting


class ReplaceFileRuleAction(RuleAction):
    def __init__(self, is_create_target_directory, target_directory_name_template, target_path=None):
        super().__init__(rule_actions_types.REPLACE_FILE):
        self._is_create_target_directory = is_create_target_directory
        self._target_directory_name_template = target_directory_name_template
        self._target_path = target_path

    @property
    def is_create_target_directory(self):
        return self._is_create_target_directory

    @property
    def target_directory_name_template(self):
        return self._target_directory_name_template

    @property
    def target_path(self):
        return self._target_path


class RenameFileRuleAction(RuleAction):
    def __init__(self, file_name_template):
        super().__init__(rule_actions_types.RENAME_FILE):
        self._file_name_template = file_name_template

    @property
    def file_name_template(self):
        return self._file_name_template


class GroupByAttributeFileRuleAction(RuleAction):
    def __init__(self, action_type, target_directory_template):
        super().__init__(action_type)
        self._target_directory_template = target_directory_template

    @property
    def target_directory_template(self):
        return self._target_directory_template
