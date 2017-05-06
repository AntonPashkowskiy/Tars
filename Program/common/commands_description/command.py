#!/usr/bin/python3


class Command:
    def __init__(self, target_block, action, additional_information):
        self._target_block = target_block
        self._action = action
        self._additional_information

    @property
    def target_block(self):
        return self._target_block

    @property
    def action(self):
        return self._action

    @property
    def additional_information(self):
        return self._additional_information