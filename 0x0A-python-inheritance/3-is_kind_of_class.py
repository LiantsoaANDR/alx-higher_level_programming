#!/usr/bin/python3
""" Module for comparison between obj and a class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the obect is an instance of, or is an instance of
    a class that inherited from, the specified class

    Args:
        obj: The object
        a_class: the specified class

    Return: True if true, Flase otherwise
    """
    return (isinstance(obj, a_class))
