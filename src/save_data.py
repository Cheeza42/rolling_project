import json
import os

def save_instance(instance_data):
    #Saves a new virtual machine instance to instances.json.
    file_path = "configs/instances.json"
  
    absolute_path = os.path.abspath(file_path)
    print(f" Saving data to: {absolute_path}")

    
    if os.path.exists(file_path):
        print(f" File already exists at: {absolute_path}")
    else:
        print(f" File does not exist yet. It will be created at: {absolute_path}")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Load existing data
    try:
        with open(file_path, "r") as f:
            instances = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        instances = []

    # Append the new instance
    instances.append(instance_data)

    # Save back to JSON file
    with open(file_path, "w") as f:
        json.dump(instances, f, indent=4)

    print(f" Machine '{instance_data['name']}' saved successfully!")

