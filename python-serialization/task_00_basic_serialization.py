#!/usr/bin/env python3
"""Serialize a dictionary to a JSON file and load it back."""
import json


def serialize_and_save_to_file(data, filename):
    """Save data to the file named filename as JSON."""
    # open the file named by filename in write mode
    with open(filename, "w") as f:
        # write data into the file as JSON
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load the JSON file named filename and return its data."""
    # open the file named by filename in JSON mode
    with open(filename, "r") as f:
        # load the JSON from the file into a variable
        data = json.load(f)
    # give the dictionary back to the caller
    return data
