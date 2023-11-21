#!/usr/bin/python3
""" Define a class Sqaure """


class Square:
    """
    Defines a squre by: (based on 0-square.py).

    Attributes:
        size: the size of a square a private instance attribute
    """
    def __init__(self, size):
        """
        Initialize the object with a specified size.

        Args:
            size: the size of a square
        """
        self.__size = size
