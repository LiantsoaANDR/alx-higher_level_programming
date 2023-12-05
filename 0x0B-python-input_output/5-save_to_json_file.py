#!/usr/bin/python3
"""Module to write an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation

    Args:
        my_obj: the object
        filename: the name of the JSON file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
