#!/usr/bin/python3
"""Module for a class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """Base Geometry class"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Check if value is an integer and is > 0

        Args:
            name: a name, as a string, that has a value
            value: the value, should be an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
