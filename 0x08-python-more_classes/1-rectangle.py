#!/usr/bin/python3
"""Define a class that defines a rectangle (based on 0-rectangle.py)"""


class Rectangle:
    """
    Defines a rectangle

    Attributes:
        width: the width of the rectangle
        height: the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle

        Args:
            width: its width
            height: its height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter

        Return: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter

        Args:
            value: the value of the width as an int and >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter

        Return: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter

        Args:
            value: the value of the height as an int and >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
