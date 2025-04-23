import sys
import os
import logging
from machine import save_vms_to_json, collect_vms  # מייבא את collect_vms מ-machine.py
import time

# Making sure that the machine recognizes the functions from the 'src' file that stored in infra_automation.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'infra_automation', 'src'))) 

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def setup_provisioning_logger():
    log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'provisioning.log')

    logger = logging.getLogger('provisioning_logger')
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def create_vm():
    logger = setup_provisioning_logger()
    logger.info("Provisioning started") 
    time.sleep(2)
    print("Starting create_vm()...")
    time.sleep(3)
    try:
        # Get the list of VMs through collect_vms
        vm_list = collect_vms()  
        
        time.sleep(2)
        
        if vm_list:
            print("\nList of all configured VMs:")
            for i, vm in enumerate(vm_list, start=1):
                time.sleep(3)
                print(f"\n--- VM {i} ---")
                time.sleep(1)
                print(vm.show_details())
                time.sleep(2)
                logger.info(f"Machine created: {vm.name}, OS: {vm.vm_os}, CPU: {vm.cpu}, RAM: {vm.ram}GB, Disk: {vm.disk_size}GB")

            save_vms_to_json(vm_list)
            time.sleep(3)  
            logger.info("Provisioning completed for all VMs.")
        else:
            logger.warning("No valid VMs were added.")

    except Exception:
        logger.exception("Provisioning failed due to an unexpected error")

if __name__ == "__main__":
    create_vm()

