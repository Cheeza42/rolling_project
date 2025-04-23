import sys
import os
import logging
from machine import save_vms_to_json, collect_vms  
import time

# Making sure that the machine recognizes the functions from the 'src' file that is stored in infra_automation.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'infra_automation', 'src'))) 

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def setup_provisioning_logger():
    # Build the absolute path (.abspath) to the logs/ directory
    log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
    os.makedirs(log_dir, exist_ok=True)  # Ensure logs directory exists

    
    log_file = os.path.join(log_dir, 'provisioning.log')

    
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
    logger = setup_provisioning_logger()  # Set up logger for provisioning process
    logger.info("Provisioning started")  
    time.sleep(2)  
    print("Starting create_vm()...")  
    time.sleep(3)  

    try:
        # Get the list of VMs through collect_vms
        vm_list = collect_vms()  # Call collect_vms() to get a list of VMs from user input
        
        time.sleep(2)  
        
        if vm_list:  # If there are valid VMs in the list
            print("\nList of all configured VMs:")  
            for i, vm in enumerate(vm_list, start=1):  # Iterate through each VM in the list
                time.sleep(3)  
                print(f"\n--- VM {i} ---")  # Print the VM index
                time.sleep(1)  
                print(vm.show_details())  # Display the details of the current VM
                time.sleep(2)  

                # Log each machine creation details
                logger.info(f"Machine created: {vm.name}, OS: {vm.vm_os}, CPU: {vm.cpu}, RAM: {vm.ram}GB, Disk: {vm.disk_size}GB")

            save_vms_to_json(vm_list)  # Save the list of VMs to a JSON file
            time.sleep(3)  
            logger.info("Provisioning completed for all VMs.")  # Log that provisioning has been completed
        else:
            # Log a warning if no valid VMs were added
            logger.warning("No valid VMs were added.")

    except Exception:
        # If an error occurs during provisioning, log the exception
        logger.exception("Provisioning failed due to an unexpected error")

if __name__ == "__main__":
    create_vm()  # Start the VM creation process when running the script

