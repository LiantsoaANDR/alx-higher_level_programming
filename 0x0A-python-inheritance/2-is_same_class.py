#!/usr/bin/python3
"""Module that check the instance"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class

    Args:
        obj: the object to check
        a_class: the specified class

    Return: True if it is true, False otherwise
    """
    return (type(obj) is a_class)
