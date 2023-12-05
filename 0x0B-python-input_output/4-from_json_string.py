#!/usr/bin/python3
"""Module: JSON string to an object (Python data structure)"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON str"""
    return json.loads(my_str)
