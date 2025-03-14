from validation import validate_input


class VirtualMachine:     # Creating a blueprint that contains criterions for the user's input. 
    def __init__(self, name: str, vm_os: str, cpu: int, ram: int, disk_size: int):
        self.name = name
        self.vm_os = vm_os
        self.cpu = cpu
        self.ram = ram
        self.disk_size = disk_size
       

    def show_details(self): # A fuction that prints the input in human readable format.
        return f"VM: {self.name}, OS: {self.vm_os}, CPU: {self.cpu} cores, RAM: {self.ram}GB, Disk size: {self.disk_size}GB."
   

   
 

    @classmethod    
 # '@classmethod'is a decorator is a special function that modifies the behavior of another function
 # or class  without changing its code directly.
 # It is marked with @ and placed above the function it affects.


    def from_user_input(cls):
       while True:
        
        name = input("Enter machine name: ")
        vm_os = input("Enter OS: ")
        cpu = int(input("Enter number of CPU cores: "))
        ram = int(input("Enter RAM size (GB): "))
        disk_size = int(input("Enter Disk size (GB): "))
       
        if validate_input((name, vm_os, cpu, ram, disk_size)):
          break
        else:
           print("Error: Invalid input. Please enter valid values.")
      
       return cls(name, vm_os, cpu, ram, disk_size) 
     
 
 # 'cls()' returns a new instance of the class with the provided data.
 # For example: Instead of manually creating an instance using VM self.(name, cpu, ram, disk, os),
 # you can call VM 'from_user_input(cls)', and it will achieve the same result.
       
VM = VirtualMachine.from_user_input()
print(VM.show_details())