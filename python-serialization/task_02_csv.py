#!/usr/bin/env python3
"""Create a csv into json file"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converting a csv to json to return list"""
    try:
        # open the CSV file in read mode
        with open(csv_filename, "r", newline="") as f:
            # read every row as a dictionary and keep them in a list
            rows = list(csv.DictReader(f))
        # open data.json in write mode
        with open("data.json", "w") as f:
            # write the list into the file as JSON
            json.dumo(rows, f)
        return True
    except Exception:
        return False
