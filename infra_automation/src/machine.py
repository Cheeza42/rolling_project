import os
import json
import time
from pydantic import BaseModel, Field

# VirtualMachine model defines the structure and validation rules for VM configuration
class VirtualMachine(BaseModel):
    # Define the fields of the VM with validations using Pydantic
    name: str = Field(..., min_length=1, description="Machine name")  
    vm_os: str = Field(..., min_length=1, description="Operating system")
    cpu: int = Field(..., gt=0, description="Number of CPU cores")
    ram: int = Field(..., gt=0, description="RAM size in GB")
    disk_size: int = Field(..., gt=0, description="Disk size in GB")

    # This function formats the VM details into a human-readable string
    def show_details(self) -> str:
        return (
            f"Machine Name: {self.name}\n"
            f"Operating System: {self.vm_os}\n"
            f"CPU Cores: {self.cpu}\n"
            f"RAM: {self.ram} GB\n"
            f"Disk Size: {self.disk_size} GB"
        )

    # Custom function to convert the model into a dictionary for JSON saving
    def to_dict(self):
        return {
            "name": self.name,
            "vm_os": self.vm_os,
            "cpu": self.cpu,
            "ram": self.ram,
            "disk_size": self.disk_size
        }

# Asks the user for VM details and returns a VirtualMachine object if valid
def get_user_input():
    error_count = 0  # The user will have only a few tries in the process. In case of failing, the code will break.
    while error_count < 3:
        try:
            # Collecting input from the user
            name = input("Enter machine name: ").strip()
            vm_os = input("Enter operating system (os): ").strip()
            cpu = int(input("Enter number of CPU cores: ").strip())
            ram = int(input("Enter RAM size (GB): ").strip())
            disk_size = int(input("Enter disk size (GB): ").strip())

            # Try to create a VirtualMachine object and validate the data
            vm = VirtualMachine(name=name, vm_os=vm_os, cpu=cpu, ram=ram, disk_size=disk_size)
            return vm  # Return the valid VM object

        except Exception as e:
            # Display an error message in case of invalid details.
            print("\nError: Invalid input. Please ensure all details are entered correctly")  
            error_count += 1
            if error_count >= 3:  # Exit the program after 3 invalid attempts
                print("\nToo many invalid attempts. Exiting program..")
                break
    return None  # Return None if too many invalid attempts

def save_vms_to_json(vm_list):
    # Use an absolute path for the file inside the 'configs' folder
    file_path = os.path.join(os.path.dirname(__file__), '..', 'configs', 'instances.json')
    file_path = os.path.abspath(file_path)  
    
    # Prints a message for showing the saving process 
    print(f"\nSaving VMs...")  
    
    time.sleep(5)  

    # Ensure the configs directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Check if the file already exists and read the existing content (to avoid overwriting)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            existing_data = json.load(f)  # Load the existing content from the JSON file
    else:
        existing_data = []  # Initialize an empty list if the file doesn't exist

    # Convert VM objects to dictionaries and append them to the existing data
    new_vms_data = [vm.to_dict() for vm in vm_list]  # Use the custom .to_dict() function to convert VMs to dicts

    # Only print and save the new data, not the entire existing content
    print(f"\nData being saved this session: {json.dumps(new_vms_data, indent=4)}")  # Show only new data to be saved

    time.sleep(5)  

    # Write the updated data to the JSON file
    with open(file_path, 'w') as f:
        json.dump(existing_data + new_vms_data, f, indent=4)  # Append new VMs to existing data
        print(f"\nVMs successfully saved!")  # Debugging message confirming that data was saved

# Function to collect multiple VMs
def collect_vms():
    vm_list = []  # Initialize an empty list to store the VMs

    while True:
        vm = get_user_input()  # Get a VM from the user

        if vm:  # If a valid VM is entered, append it to the list
            vm_list.append(vm)

        # Ask if the user wants to add another machine
        add_another = input("\nWould you like to add another VM? (yes/no): ").strip().lower()
        if add_another != "yes":  # If the user doesn't want to add another machine, break the loop
            break

    return vm_list  # Return the list of VMs


   

