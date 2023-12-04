#!/usr/bin/python3
"""Module to list available attributes and methods of an object"""


def lookup(obj):
    """
    Finds all the available attributes and methods of an object

    Args:
        obj: the object
    Return: a list of available attributes and methods of an object
    """
    return dir(obj)
