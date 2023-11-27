#!/usr/bin/python3
"""Define a class that defines a rectangle (based on 2-rectangle.py)"""


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

    def area(self):
        """
        Calculates the area of the rectangle

        Return: the area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Return: the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Draws the rectangle with the character #

        Return: the rectangle as a string
        """
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect

        for i in range(0, self.__height):
            rect += "#" * self.__width
            rect += "\n"
        return rect
