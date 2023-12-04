#!/usr/bin/python3
""" Module for comparaison betzeen obj and a class """


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited 
    (directly or indirectly) from the specified class

    Args:
        obj: the object
        a_class: the specified class

    Return: True if true, Fasle otherwise
    """
    return (isinstance(obj, a_class) and type(obj) is not a_class)
