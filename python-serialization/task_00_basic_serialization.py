#!/usr/bin/python3

import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary into JSON and save it to a file.

    Parameters:
        data (dict): The dictionary to serialize.
        filename (str): Path to the output JSON file. Overwrites if exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f , indent=4)

def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it back into a Python dictionary.

    Parameters:
        filename (str): Path to the input JSON file.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
