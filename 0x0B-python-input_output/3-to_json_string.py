#!/usr/bin/python3
"""Module for a representation of a object to a JSON"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string):"""
    return json.dumps(my_obj)
