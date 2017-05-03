from messaging.messaging_manager import MessagingManager, MessagingManagerType
from common.monitoring import monitor_event_types as event_types

from inotify.adapters import Inotify
from inotify import constants as inotify_constants
from threading import Event, Timer
from pprint import pprint


__event_type_to_flag_mapping = {
    event_types.FILE_CREATED: inotify_constants.IN_CREATE,
    event_types.FILE_NAME_CHANGED: inotify_constants.IN_MOVE,
    event_types.FILE_CONTENT_CHANGED: inotify_constants.IN_MODIFY,
    event_types.FILE_INCLUDED: inotify_constants.IN_MOVED_TO,
    event_types.FILE_EXCLUDED: inotify_constants.IN_MOVED_FROM,
    event_types.FILE_DELETED: inotify_constants.IN_DELETE,
    event_types.FILE_METADATA_CHANGED: inotify_constants.IN_ATTRIB,
    event_types.DIRECTORY_REPLACED: inotify_constants.IN_MOVE_SELF,
    event_types.DIRECTORY_DELETED: inotify_constants.IN_DELETE_SELF
}


def get_message_by_event(event):
    (header, type_names, watch_path, file_name) = event
    pprint(event)


def get_message_by_event_pair(first_event, second_event):
    return "Event pair"


def is_first_pair_event(event_header):
    return event_header.mask == inotify_constants.IN_MOVED_FROM


def is_second_pair_event(event_header):
    return event_header.mask == inotify_constants.IN_MOVED_TO


def process_possible_pair_event(current_event, pair_event_list):
    (header, _, watch_path, _) = current_event

    if len(pair_event_list) == 0 and is_first_pair_event(header):
        pair_event_list.append(current_event)
        return []
    elif len(pair_event_list) != 0:
        previous_event = pair_event_list.pop()
        (_, _, previous_watch_path, _) = previous_event

        if previous_watch_path == watch_path and is_second_pair_event(header):
            pair_events_message = get_message_by_event_pair(previous_event, current_event)
            return [ pair_events_message ]
        else:
            previous_event_message = get_message_by_event(previous_event)
            current_event_message = get_message_by_event(current_event)
            return [ previous_event_message, current_event_message ]
    return None


def process_recieved_messages(monitor, messages_list):
    print("message processing")
    pass


def process_recieved_events(monitor, monitor_messaging_manager, pair_events_list, stop_events_processing_flag):
    for event in monitor.event_gen():
        if event is not None:
            messages = process_possible_pair_event(event, pair_events_list)

            if messages is None:
                message = get_message_by_event(event)
                print(message or "lol")
            else:
                for message in messages:
                    print(message or "lol")
        else:
            if stop_events_processing_flag.is_set():
                stop_events_processing_flag.clear()
                break

            
def main():
    monitor = Inotify()
    monitor_messaging_manager = MessagingManager(MessagingManagerType.SERVER)
    watch_paths_list = [ b'/home/anton/test/' ]
    pair_events_list = []
    stop_events_processing_flag = Event()

    for path in watch_paths_list:
        monitor.add_watch(path, inotify_constants.IN_MOVE | inotify_constants.IN_MOVED_TO | inotify_constants.IN_MOVED_FROM | inotify_constants.IN_CREATE)

    try:      
        while True:
            messages = monitor_messaging_manager.get_all_recieved_messages()
            process_recieved_messages(monitor, messages)
            
            stop_events_processing_timer = Timer(10, stop_events_processing_flag.set)
            stop_events_processing_timer.start()
            process_recieved_events(monitor, monitor_messaging_manager, pair_events_list, stop_events_processing_flag)

    except KeyboardInterrupt:
        for path in watch_paths_list:
            monitor.remove_watch(path)
        raise SystemExit()


if __name__ == "__main__":
    main()
