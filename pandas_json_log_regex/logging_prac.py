import logging


# Set the logging configuration
logging.basicConfig(
    filename='app_log',                                   # Specify the log file
    level=logging.ERROR,                                   # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s',    # Specify the log message format
    handlers=[
        logging.FileHandler("app.log"), # keep log in file
        logging.StreamHandler() #to print logs on console
    ]
)

# Log some messages
logging.debug('This is a debug message')
logging.info('This is an informational message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')