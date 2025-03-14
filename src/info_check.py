"""
 A function that validates the input information.
 if any of the info is invalid:
 the function will return an error message 
 
"""

def validate_input(data):

    name, vm_os, cpu, ram, disk_size  = data 



    if not name or cpu <= 0 or ram <= 0 or disk_size <= 0 or not vm_os:
         print("Invalid input detected. Please insert valid values.")
         return False
    
    return True
    
  