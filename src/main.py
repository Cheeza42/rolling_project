from info_check import validate_input
from save_data import save_instance 

class VirtualMachine:     # Creating a blueprint that contains criterions for the user's input. 
    def __init__(self, name: str, vm_os: str, cpu: int, ram: int, disk_size: int):
       
        self.name = name
        self.vm_os = vm_os
        self.cpu = cpu
        self.ram = ram
        self.disk_size = disk_size
   
    def show_details(self): # A fuction that prints the input in human readable format.    
        return (f"Machine Name: {self.name}\n"
                f"Operating System: {self.vm_os}\n"
                f"CPU Cores: {self.cpu}\n"
                f"RAM: {self.ram} GB\n"
                f"Disk Size: {self.disk_size} GB")
   
    def to_dict(self):
        return {
            "name": self.name,
            "vm_os": self.vm_os,
            "cpu": self.cpu,
            "ram": self.ram,
            "disk_size": self.disk_size
        }
   
   
    @classmethod    
 # '@classmethod'is a decorator is a special function that modifies the behavior of another function
 # or class  without changing its code directly.
 # It is marked with @ and placed above the function it affects. 
    def from_user_input(cls):
        while True:
            try:
                name = input("Enter machine name: ")
                vm_os = input("Enter OS: ")
                cpu = input("Enter number of CPU cores: ")
                ram = input("Enter RAM size (GB): ")
                disk_size = input("Enter Disk size (GB): ")       
                validated_data = validate_input((name, vm_os, cpu, ram, disk_size))
                if validated_data:
                   break
                else:
                    print("Invalid input. Please ensure all fields are correctly filled.")
            except ValueError():
              print("Invalid input. Please ensure all fields are correctly filled.")                                                                    
              continue
       
        return cls(name, vm_os, cpu, ram, disk_size)
 
 # 'cls()' returns a new instance of the class with the provided data.
 # For example: Instead of manually creating an instance using VM self.(name, cpu, ram, disk, os),
 # you can call VM 'from_user_input(cls)', and it will achieve the same result.   


VM = VirtualMachine.from_user_input()
print(VM.show_details())


save_instance(VM.to_dict())

