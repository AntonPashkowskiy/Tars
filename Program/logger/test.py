#!/usr/bin/python3
from logger.logger_module import LoggerModule


def main():
    logger_module = LoggerModule("/home/anton/test/tars.log", None)
    logger_module.logger.info("Test info")
    logger_module.logger.debug("Debug info")
    logger_module.logger.error("Error info")


if __name__ == "__main__":
    main()