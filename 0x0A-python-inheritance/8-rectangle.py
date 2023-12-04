#!/usr/bin/python3
"""Module for Rectangle, inherits from BaseGeometry (7-base_geometry.py)"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a rectangle

    Attributes:
        width: the width of the rectangle
        height: the height of the rectangle
    """
    def __init__(self, width, height):
        """
        Initialize the rectangle

        Args:
            width: its width
            height: its height
        """
        self.integer_validator(width, int)
        self.integer_validator(height, int)
        self.__width = width
        self.__height = height
