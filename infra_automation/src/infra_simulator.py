import sys
import os
import logging
from machine import get_user_input, save_vms_to_json

# Making sure that the machine recognize the functions from the 'src' file that stored in ifra_automation.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'infra_automation', 'src'))) 

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def setup_provisioning_logger():
    # Build the absolute path (.abspath) to the logs/ directory
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

    return logger

def create_vm():
    logger = setup_provisioning_logger()
    logger.info("Provisioning started") 
    print("Starting create_vm()...")

    try:
        # Create a VirtualMachine object using the VirtualMachine class
        vm = get_user_input()  
    
        if vm:
            # Display machine details
            print("\nMachine Details:")
            print(vm.show_details())

            # Save the machine information as a dictionary and turn it into JSON
            save_vms_to_json([vm])  
            print("\nMachine in dictionary format:")

            # Log the machine creation with its details
            logger.info(f"Machine created: {vm.name}, OS: {vm.vm_os}, CPU: {vm.cpu}, RAM: {vm.ram}GB, Disk: {vm.disk_size}GB")
            logger.info(f"Provisioning completed for VM: {vm.name}")
        else:
            logger.warning("No valid VM was created after 3 failed attempts.")

    except Exception:
        logger.exception("Provisioning failed due to an unexpected error")

if __name__ == "__main__":
    create_vm()

