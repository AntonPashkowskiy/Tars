#!/usr/bin/python3
from commands_description.commands_description_module import CommandsDescriptionModule
from common.commands_description.command import Command
from common.commands_description import target_block_types, action_types


def main():
    commands_description_module = CommandsDescriptionModule()
    command = Command(target_block_types.RUSES_MANAGEMENT_BLOCK, action_types.CREATE, None)
    commands_description_module.execute_command(command)


if __name__ == "__main__":
    main()
