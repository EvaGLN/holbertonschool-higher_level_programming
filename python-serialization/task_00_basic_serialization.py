#!/usr/bin/env python3
"""Basic Serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """serialize and save a Python dictionary to a JSON file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """load and deserialize the JSON file to recreate the Python Dictionary"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
