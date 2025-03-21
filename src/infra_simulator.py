import logging
from main import VirtualMachine  # Import the VirtualMachine class from main.py

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def create_vm():
    # Create a VirtualMachine object using the VirtualMachine class
    vm = VirtualMachine()  
    
    # Display machine details
    print("\nMachine Details:")
    print(vm.show_details())  # Display machine details using show_details()

    # Save the machine information as a dictionary (this is already done in the class)
    machine_dict = vm.to_dict()  
    print("\nMachine in dictionary format:")
    print(machine_dict)

    # Log the machine creation with its details
    logging.info(f"Machine created: {vm.name}, OS: {vm.vm_os}, CPU: {vm.cpu}, RAM: {vm.ram}GB, Disk: {vm.disk_size}GB")

if __name__ == "__main__":
    create_vm()  # Call the function to create the machine and display its details
