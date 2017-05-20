from commands_description.commands_description_module import CommandsDescriptionModule
from common.commands_description import target_block_types as tbt, action_types as att
from common.commands_description.command import Command

import unittest


class CommandsDescriptionModuleTest(unittest.TestCase):
    def setUp(self):
        self.commands_module = CommandsDescriptionModule()

    def test_executing_none_command(self):
        with self.assertRaises(ValueError):
            self.commands_module.execute_command(None)

    def test_not_implemented_command(self):
        with self.assertRaises(NotImplementedError):
            bad_command = Command(tbt.EVENT_LOG_BLOCK, att.CREATE, None)
            self.commands_module.execute_command(bad_command)

    def test_read_setting_command(self):
        read_command = Command(tbt.SETTINGS_BLOCK, att.READ, None)
        setting = self.commands_module.execute_command(read_command)
        key, value = setting

        self.assertIs(type(setting), tuple)
        self.assertIsNotNone(key)
        self.assertIsNotNone(value)


if __name__ == "__main__":
    unittest.main()