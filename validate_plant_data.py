import json
import os

def validate_plant_data(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print(f"Error: {file_path} is not a valid JSON file.")
            return False

    required_fields = [
        "name", "scientific_name", "family", "description", 
        "growth_characteristics", "environmental_requirements", 
        "cultivation_info", "visual_characteristics", "3d_model_file"
    ]
    
    for field in required_fields:
        if field not in data:
            print(f"Error: {file_path} is missing the required field '{field}'")
            return False
    
    print(f"Validation successful for {file_path}")
    return True

def validate_all_plants():
    data_dir = "data"
    plant_files = ["tomato.json", "cucumber.json", "basil.json", "bell_pepper.json", "strawberry.json"]
    
    for filename in plant_files:
        file_path = os.path.join(data_dir, filename)
        if os.path.exists(file_path):
            validate_plant_data(file_path)
        else:
            print(f"Warning: {filename} does not exist in the data directory.")

if __name__ == "__main__":
    validate_all_plants()
