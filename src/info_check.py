"""
 A function that validates the input information.
 if any of the info is invalid:
 the function will return an error message 
 
"""


import re   # The 're' module in Python provides tools for working with Regular Expressions (regex).
            # It allows pattern-based searching, validation, and text extraction for the code.
            # Here we used 're.fullmatch()' to validate each parameter from the beginning of the string.
            # '\d' in regex says that is numbers, and we added '+' because it appears more the once.


def validate_input(data):
    try:
        name, vm_os, cpu, ram, disk_size = data

        # 🖥️ Ensure all inputs are treated as strings
        name, vm_os, cpu, ram, disk_size = map(str, [name, vm_os, cpu, ram, disk_size])

        # 🖥️ Validate that machine name and OS name are not only numbers
        if re.fullmatch(r"\d+", name.strip()) or re.fullmatch(r"\d+", vm_os.strip()):
            return False

        # 🔢 Convert CPU, RAM, and Disk Size to integers before validation
        try:
            cpu, ram, disk_size = int(cpu), int(ram), int(disk_size)
        except ValueError:
            return False

        # 🔢 Ensure CPU, RAM, and Disk Size are positive integers
        if cpu <= 0 or ram <= 0 or disk_size <= 0:
            return False

        return name, vm_os, cpu, ram, disk_size  # מחזיר את הנתונים התקינים

    except ValueError:
        print("Invalid input. Please ensure all fields are correctly filled.")
        return False


