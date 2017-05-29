from threading import Thread, Event
from common.utils.singleton import Singleton


class MonitorMessagesProcessingLoop(Thread):
    def __init__(self, messaging_manager, stop_event):
        super().__init__()
        self._stop_event = stop_event
        self._messaging_manager = messaging_manager

    def _process_messages(self, messages):
        for message in messages:
            event = _parse_message(message)
            analysis_result = FileAnalyzer.analyse_file(event.target_file)
            rules = _rules_manager.get_rules(event, analysis_result)
            
            if not len(rules):
                pass
            elif _is_delete_rule(rules[0]):
                _delete_file(event.target_file, rules[0])
            else:
                _apply_rules(event, rules)

    def run(self):
        while not self._stop_event.is_set():
            if not self._messaging_manager.is_recieved_messages_exists():
                continue

            self._process_messages(self._messaging_manager.get_all_recieved_messages())


class MonitorInteractionManager(metaclass=Singleton):
    def __init__(self):
        self._send_queue = None
        self._receive_queue = None
        self._logger_module = None
        self._settings_module = None
        self._messaging_manager = MessagingManager(MessagingManagerType.CLIENT, "tcp://127.0.0.1:5555")
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