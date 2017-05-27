#!/usr/bin/python3


class Rule:
    def __init__(self, target_directory, file_constraints, action):
        self._target_directory = target_directory
        self._file_constraints = file_constraints
        self._action = action

    @property
    def target_directory(self):
        return self._target_directory

    @property
    def file_constraints(self):
        return self._file_constraints

    @property
    def action(self):
        return self._action
