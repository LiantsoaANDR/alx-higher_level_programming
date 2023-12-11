#!/usr/bin/python3
"""Module for our base of all other classes in this project"""
from json import dumps


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

    def int_validator(self, name, value, flag):
        """
        Check if value is an integer and is > 0 if it's a measurement
        , >= 0 if it's a position

        Args:
            name: a name, as a string, that has a value
            value: the value, should be an integer
            flag: if flag is 0, value will be treated as a measurement
                  if flag is 1, value will be treated as a position
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0 and flag == 0:
            raise ValueError("{} must > 0".format(name))

        if value < 0 and flag == 1:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Transforms a dictionary into a JSON string

        Args:
            list_dictionaries: the dictionary

        Return: the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        Args:
            list_objs: is a list of instances who inherits of Base
                       example: list of Rectangle or list of Square instances
        """
