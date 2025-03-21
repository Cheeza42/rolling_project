import os
import json
from pydantic import BaseModel, Field

# VirtualMachine model defines the structure and validation rules for VM configuration
class VirtualMachine(BaseModel):
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

# Asks the user for VM details
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
            return vm

        except Exception as e:
            # Display an error message in case of invalid details.
            print(f"\nError: {str(e)}")  # Use str(e) to get the error message from the exception
            error_count += 1
            if error_count >= 3:
                print("\nToo many invalid attempts. Exiting program..")
                break
    return None

def save_vms_to_json(vm_list):
    # Use an absolute path for the file inside the 'configs' folder
    file_path = os.path.join(os.getcwd(), 'configs', 'instances.json')

    # Debugging: print the path to ensure it's correct
    print(f"\nSaving VMs...")
    
    # Check if the file already exists and read the existing content (to avoid overwriting)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            existing_data = json.load(f)  # Load the existing content from the JSON file
    else:
        existing_data = []  # Initialize an empty list if the file doesn't exist

    # Convert VM objects to dictionaries and append them to the existing data
    new_vms_data = [vm.to_dict() for vm in vm_list]  # Use the custom .to_dict() function
    existing_data.extend(new_vms_data)

    # Debugging: print the data we're about to save
    print(f"\nData being saved: {json.dumps(existing_data, indent=4)}")

    # Write the updated data to the JSON file
    with open(file_path, 'w') as f:
        json.dump(existing_data, f, indent=4)
        print(f"\nVMs successfully saved!")  # Debugging: confirm saving

# Condition that adds the valid VMs to a list (in case the user added multiple machines)
if __name__ == "__main__":
    vm_list = []

    while True:
        vm = get_user_input()

        if vm:
            vm_list.append(vm)

        add_another = input("\nWould you like to add another VM? (yes/no): ").strip().lower()
        if add_another != "yes":
            break

    # Display the list of valid machines after input is finished
    if vm_list:
        print("\nList of all configured VMs:")
        for i, vm in enumerate(vm_list, start=1):
            print(f"\n--- VM {i} ---")
            print(vm.show_details())

        # Ensure that we save the VMs after displaying them
        save_vms_to_json(vm_list)

    elif not vm_list:
        print("\nNo valid VMs were added.")
