from messaging.messaging_manager import MessagingManager, MessagingManagerType
from common.monitoring import monitor_event_types as event_types
from inotify.adapters import Inotify
from inotify import constants as inotify_constants
from pprint import pprint

__event_type_to_flag_mapping = {
    event_types.INNER_OBJECT_CREATED: inotify_constants.IN_CREATE,
    event_types.INNER_OBJECT_NAME_CHANGED: 0,
    event_types.INNER_OBJECT_CONTENT_CHANGED: 0,
    event_types.INNER_OBJECT_INCLUDED: 0,
    event_types.INNER_OBJECT_EXCLUDED: 0,
    event_types.INNER_OBJECT_DELETED: 0,
    event_types.DIRECTORY_NAME_CHANGED: 0,
    event_types.DIRECTORY_REPLACED: 0,
    event_types.DIRECTORY_DELETED: 0
}

def process_recieved_messages(monitor, messages_list):
    pass


def get_message_by_event(event):
    pprint(event)


def main():
    monitor = Inotify()
    monitor_messaging_manager = MessagingManager(MessagingManagerType.SERVER)
    watch_paths_list = [ b'/home/anton/' ]

    for path in watch_paths_list:
        monitor.add_watch(path)

    try:      
        while True:
            messages = monitor_messaging_manager.get_all_recieved_messages()
            process_recieved_messages(monitor, messages)

            for event in monitor.event_gen():
                if event is not None:
                    message = get_message_by_event(event)
                    #print(message)
    except KeyboardInterrupt:
        for path in watch_paths_list:
            monitor.remove_watch(path)
        raise SystemExit()


if __name__ == "__main__":
    main()
