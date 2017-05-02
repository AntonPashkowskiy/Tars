__delimeter = " : "

class MonitorMessage:
    def __init__(self, event):
        self._target_directory = ""
        self._target_file = ""
        self._additional_information = ""
        self._event_type = 0
        self._delimeter = " : "

    def __repr__(self):
        return __combine_message()

    def __str__(self):
        return __combine_message()

    def __combine_message(self):
        return __delimeter.join([self._target_directory, self._target_file, self._additional_information, self._event_descriptor])

    @property
    def target_directory(self):
        return self._target_directory

    @target_directory.setter
    def target_directory(self, value):
        self._target_directory = value

    @property
    def target_file(self):
        return self._target_file

    @target_file.setter
    def target_file(self, value):
        self._target_file = value

    @property
    def additional_information(self):
        return self._additional_information

    @additional_information.setter
    def additional_information(self, value):
        self._additional_information = value

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value

    @staticmethod
    def restore_from_string(message):
        message_object = MonitorMessage()

        if (message != None):
            message_object.target_directory, message_object.target_file, type_string = message.split(__delimter)
            message_object.event_type = int(type_string)
            return message_object
        return None




    