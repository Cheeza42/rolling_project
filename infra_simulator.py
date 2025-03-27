import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'infra_automation', 'src'))) 
import logging
from machine import get_user_input, save_vms_to_json
from logger import setup_provisioning_logger




# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def create_vm():
   logger = setup_provisioning_logger()
   logger.info("Provisioning started") 
   print("Starting create_vm()...")   # Import the VirtualMachine class from main.py

   try:
    # Create a VirtualMachine object using the VirtualMachine class
    vm = get_user_input()  
    
    if vm:
        # Display machine details
       print("\nMachine Details:")
       print(vm.show_details())  # Display machine details using show_details()

    # Save the machine information as a dictionary and turn it into JSON (by the fuction that was imported from 'machine.py')
       save_vms_to_json([vm])  
       print("\nMachine in dictionary format:")
       

       # Log the machine creation with its details
       logger.info(f"Machine created: {vm.name}, OS: {vm.vm_os}, CPU: {vm.cpu}, RAM: {vm.ram}GB, Disk: {vm.disk_size}GB")


       logger.info(f" Provisioning completed for VM: {vm.name}")
    else:
       logger.warning("No valid VM was created after 3 failed attempts.")

   except Exception:
    logger.exception(" Provisioning failed due to an unexpected error")

if __name__ == "__main__":
    create_vm()  # Call the function to create the machine and display its details
