import logging
import os

# This function sets up a logger that writes to logs/provisioning.log
def setup_provisioning_logger():
    # Build the absolute path (.abspath) to the logs/ directory and make sure it will find it no matter where its been placed in the project's SETUP
    log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
    
    # Make sure the logs directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Define the full path to the log file
    log_file = os.path.join(log_dir, 'provisioning.log')

    # Create or get a logger named 'provisioning_logger'
    logger = logging.getLogger('provisioning_logger')
    logger.setLevel(logging.INFO)

    # Prevent adding multiple handlers if the logger is reused
    if not logger.handlers:
        
        # Create a file handler that writes to provisioning.log
        file_handler = logging.FileHandler(log_file)

        # Define the log message format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

    # Return the configured logger
    return logger
