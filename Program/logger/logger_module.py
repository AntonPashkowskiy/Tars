from common.utils.singleton import Singleton

import logging as LOG


class LoggerModule(metaclass=Singleton):
    def __init__(self, filename, database):
        LOG.basicConfig(level=LOG.DEBUG,
                        format='%(levelname)s [%(asctime)s]: %(message)s', 
                        datefmt='%m-%d-%y %I:%M:%S',
                        filename=filename,
                        filemode='a')

    def log_fs_event_information(self, fs_event_info):
        pass

    def read_fs_events(self, start_date, end_date):
        pass

    @property
    def logger(self):
        return LOG.getLogger('')
