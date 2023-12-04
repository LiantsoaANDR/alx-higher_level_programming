#!/usr/bin/python3
"""
Module for Square,  that inherits from Rectangle (9-rectangle.py)
(task based on 10-square.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a square

    Attributes:
        width: the width of the rectangle
        height: the height of the rectangle
    """
    def __init__(self, size):
        """
        Initialize the square

        Args:
            size: the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """print() should print, and str() should return a msg"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
