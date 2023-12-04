#!/usr/bin/python3
"""
Module for Rectangle, inherits from BaseGeometry (7-base_geometry.py)
(task based on 8-rectangle.py)
"""
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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """print() should print, and str() should return a msg"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
