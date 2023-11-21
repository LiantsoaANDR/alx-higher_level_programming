#!/usr/bin/python3
""" Define a class Square """


class Square:
    """
    defines a square by: (based on 5-square.py)

    Attributes:
        size: the size of a square, a private instance attribute.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the object with a specified size.

        Args:
            size: the size of a square
            position: a tuple of 2 ints that indicate where the
                      square begins to spawn
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ Returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Property setter of the position of the square

        Args:
            value: the position of the square
                   must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        position should be use by using space
        Don’t fill lines by spaces when position[1] > 0
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                space = " " * self.__position[0]
                sqr = "#" * self.__size
                print("{}{}".format(space, sqr))
