#!/usr/bin/python3
"""Module for our base of all other classes in this project"""


class Base:
    """
    This class is the 'base' of all other classes in this project

    Attributes:
        __nb_objects: the number of objects
        id: the id of the object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the new object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
