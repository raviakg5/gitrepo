import os
import logging


class CustomLogger:
    def __init__(self, filename, log_dir):
        self.filename = filename
        self.log_dir = log_dir
        self.logger = None

    def create_logger(self):
        # Create the log directory if it does not exist
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        # Create a logger object
        self.logger = logging.getLogger(self.filename)
        self.logger.setLevel(logging.DEBUG)

        # Create a file handler and set its log level to DEBUG
        file_handler = logging.FileHandler(os.path.join(self.log_dir, self.filename))
        file_handler.setLevel(logging.DEBUG)

        # Create a log formatter and add it to the file handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        self.logger.addHandler(file_handler)

    def log(self, level, message):
        if self.logger is None:
            self.create_logger()
        if level == 'debug':
            self.logger.debug(message)
        elif level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)
        else:
            raise ValueError(f"Invalid log level: {level}")