from threading import Thread, Event
from common.utils.singleton import Singleton


class MonitorMessagesProcessingLoop(Thread):
    def __init__(self, messaging_manager, stop_event):
        super().__init__()
        self._message_ready_event = Event()
        self._stop_event = stop_event
        self._messaging_manager = messaging_manager

    def _process_messages(self, messages):
        pass

    def run(self):
        while not self._stop_event.is_set():
            if self._message_ready_event.is_set():
                self._message_ready_event.clear()
            else:
                continue

            self._process_messages(self._messaging_manager.get_all_recieved_messages())


class MonitorInteractionManager(metaclass=Singleton):
    def __init__(self):
        self._logger_module = None
        self._settings_module = None
        self._messaging_manager = None
        self._rules_manager = None
        self._stop_event = Event()
        self._processing_loop = MonitorMessagesProcessingLoop(self._messaging_manager, self._stop_event)
        self._processing_loop.start()

    def __del__():
        self._stop_event.set()

    def _add_watching_directory_handler(self, directory_path):
        pass

    def _remove_watching_direcotory_handler(self, directory_path):
        pass

    def execute_action_immediately(self, file_path, action):
        pass

    def start_monitor(self):
        pass

    def stop_monitor(self):
        pass