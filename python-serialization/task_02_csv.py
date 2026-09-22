#!/usr/bin/env python3
"""Converting CSV Data to JSON Format"""
import csv
import json


def convert_csv_to_json(filename):
    """ takes CSV filename as parameter and writes JSON data to data.json"""
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(rows, f)
        return True
    except (FileNotFoundError, PermissionError, IsADirectoryError,
            UnicodeDecodeError, csv.Error):
        return False
