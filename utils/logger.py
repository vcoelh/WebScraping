import logging 

class LoggerClass:
    def __init__(self, log_file = 'debug.log', log_level = 'INFO'):
        log_format = "%(asctime)s:[%(levelname)s]:%(message)s"
        self.logger = logging.getLogger(log_file)
        
        logging.basicConfig(
                            level=logging.INFO, 
                            format=log_format, 
                            datefmt="[%Y-%m-%d %H:%M:%S]",
                            handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
                            )
        
        # Create a FileHandler to write log messages to the specified log file
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(log_format))
        self.logger.addHandler(file_handler)
        
        if log_level == "INFO":
            self.logger.setLevel(logging.INFO)
        elif log_level == "ERROR":
            self.logger.setLevel(logging.ERROR)
        elif log_level == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
    
    
    def info(self, message):
        self.logger.info(message)
        
    def error(self, message):
        self.logger.error(message)