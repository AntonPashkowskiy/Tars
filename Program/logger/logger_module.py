from common.utils.singleton import Singleton

import logging as LOG


class LoggerModule(metaclass=Singleton):
    def __init__(self, filename, database):
        LOG.basicConfig(level=LOG.DEBUG,
                        format='%(levelname)s [%(asctime)s]: %(message)s', 
                        datefmt='%m-%d-%y %I:%M:%S',
                        filename=filename,
                        filemode='a')

    def write_event_info(self, log_record):
        pass

    def read_event_info(self, log_record_id):
        pass

    def read_events_info_range(self, start_record_id, end_record_id):
        pass

    def read_events_info_daterange(self, start_date, end_date):
        pass

    @property
    def logger(self):
        return LOG.getLogger('')
