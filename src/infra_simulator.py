import logging
from machine import  get_user_input, save_vms_to_json   # Import the VirtualMachine class from main.py

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def create_vm():
    
    print("Starting create_vm()...")

    # Create a VirtualMachine object using the VirtualMachine class
    vm = get_user_input()  
    
    if vm:
        # Display machine details
       print("\nMachine Details:")
       print(vm.show_details())  # Display machine details using show_details()

    # Save the machine information as a dictionary and turn it into JSON (this is already done in the class)
       save_vms_to_json([vm])  
       print("\nMachine in dictionary format:")
       

    # Log the machine creation with its details
    logging.info(f"Machine created: {vm.name}, OS: {vm.vm_os}, CPU: {vm.cpu}, RAM: {vm.ram}GB, Disk: {vm.disk_size}GB")

if __name__ == "__main__":
    create_vm()  # Call the function to create the machine and display its details
