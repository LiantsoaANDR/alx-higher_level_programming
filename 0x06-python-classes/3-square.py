#!/usr/bin/python3
""" Define a class Square """


class Square:
    """
    defines a square by: (based on 2-square.py)

    Attributes:
        size: the size of a square, a private instance attribute.
    """
    def __init__(self, size=0):
        """
        Initialize the object with a specified size.

        Args:
            size: the size of a square
                  Must be an integer,  otherwise raise a TypeError exception
                  with the message size must be an integer
                  If size is less that 0, raise a ValueError exception
                  with the message size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square

        Returns: the current square area
        """
        return (self.__size ** 2)
