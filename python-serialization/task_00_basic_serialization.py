import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize the input data into JSON format and save it to a file.

    Parameters:
    data (dict): The data to be serialized.
    filename (str): The name of the file to save the serialized data to.

    Returns:
    None
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
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
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading data from file: {e}")
        return None

