import csv
import json

def convert_csv_to_json(input_filename, output_filename='data.json'):
    """
    Converts a CSV file to JSON format.

    Parameters:
    input_filename (str): The name of the CSV file to convert.
    output_filename (str): The name of the JSON file to save the data to. Default is 'data.json'.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(input_filename, 'r') as csv_file:
            # Convert each row into a dictionary
            data = list(csv.DictReader(csv_file))

        with open(output_filename, 'w') as json_file:
            # Serialize the list of dictionaries
            json.dump(data, json_file)

        # Conversion was successful
        return True
    except Exception as e:
        # An error occurred
        print(f"Error during conversion: {e}")
        return False

