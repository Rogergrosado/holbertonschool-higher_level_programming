import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize the input data into JSON format and save it to a file.

    Parameters:
    data (dict): The data to be serialized.
    filename (str): The name of the file to save the serialized data to. If the file exists, it will be replaced.

    Returns:
    None
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Data serialized and saved to '{filename}'.")
    except (IOError, TypeError) as e:
        print(f"Error saving data to file: {e}")

def load_and_deserialize(filename):
    """
    Load data from a file and deserialize it from JSON format.

    Parameters:
    filename (str): The name of the file to load the data from.

    Returns:
    dict: The deserialized data.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"Data deserialized from '{filename}'.")
            return data
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading data from file: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Output the deserialized data
    print("Deserialized Data:")
    print(deserialized_data)

