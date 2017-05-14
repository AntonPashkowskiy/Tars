#!/usr/bin/python3


class RuleFileConstraint:
    def __init__(self):
        self._is_directory = False
        self._target_event_types = []
        self._target_content_types = []
        self._target_name_template = None
        self._target_extention_template = None
        self._target_file_max_size = None
        self._target_file_min_size = None

    @property
    def is_directory(self):
        return self._is_directory

    @is_directory.setter
    def is_directory(self, value):
        self._is_directory = value

    @property
    def target_event_types(self):
        return self._target_event_types

    @target_event_types.setter
    def target_event_types(self, value):
        self._target_event_types = value

    @property
    def target_content_types(self):
        return self._target_content_types

    @target_content_types.setter
    def target_content_types(self, value):
        self._target_content_types = value

    @property
    def target_name_template(self):
        return self._target_name_template

    @target_name_template.setter
    def target_name_template(self, value):
        self._target_name_template = value

    @property
    def target_extention_template(self):
        return self._target_extention_template

    @target_extention_template.setter
    def target_extention_template(self, value):
        self._target_extention_template = value

    @property
    def target_file_max_size(self):
        return self._target_file_max_size

    @target_file_max_size.setter
    def target_file_max_size(self, value):
        self._target_file_max_size = value

    @property
    def target_file_min_size(self):
        return self._target_file_min_size

    @target_file_min_size.setter
    def target_file_min_size(self, value):
        self._target_file_min_size = value
