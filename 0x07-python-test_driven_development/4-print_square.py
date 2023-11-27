#!/usr/bin/python3
""" Module to print a square """


def print_square(size):
    """
    prints a square with the character #.

    Args:
        size: the size lenght of the square, as an int
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for height in range(0, size):
        line = "#" * size
        print("{}".format(line))
