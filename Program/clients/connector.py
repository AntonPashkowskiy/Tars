from messaging_manager import MessagingManager, MessagingManagerType
from commands_description.commands_description_module import CommandsDescriptionModule

from threading import Event


def _process_incoming_command(serialized_command, command_description_module):
    pass


def main():
    messaging_manager = MessagingManager(MessagingManagerType.SERVER, "tcp://127.0.0.1:5556")
    command_description_module = CommandsDescriptionModule()

    while True:
        if not messaging_manager.is_recieved_messages_exists():
            continue
        result = _process_incoming_commands(messaging_manager.recieve_message(), command_description_module)
        if result is not None:
            messaging_manager.send_message(result)


if __name__ == "__main__":
    main() 