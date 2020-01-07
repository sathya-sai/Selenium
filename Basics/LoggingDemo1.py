"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium logging
"""
import logging


class Logging:
    def logging(self):
        logging.debug("this is a debug message")
        logging.info("this is a info message")

        logging.warning("this is a warning message")
        logging.error("this is a error message")
        logging.critical("this is a critical message")


if __name__ == '__main__':
    l = Logging()
    l.logging()
