#!/usr/bin/python3
""" Define a class Square """


class Square:
    """
    defines a square by: (based on 4-square.py)

    Attributes:
        size: the size of a square, a private instance attribute.
    """
    def __init__(self, size=0):
        """
        Initialize the object with a specified size.

        Args:
            size: the size of a square
        """
        self.__size = size

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter of the size of the square

        Args:
            value: the size of a square
                  Must be an integer,  otherwise raise a TypeError exception
                  with the message size must be an integer
                  If size is less that 0, raise a ValueError exception
                  with the message size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square

        Returns: the current square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints in stdout the square with the character #
        If the size of the square is 0, print an empy line
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                to_print = "#" * self.__size
                print("{}".format(to_print))
