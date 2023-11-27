#!/usr/bin/python3
""" Module that contains an addition function """


def add_integer(a, b=98):
    """
    Adds 2 integers

    Args:
        a: the first argument, should be an int
        b: the second argument, initialized to 98, should be an int

    Return: the addition of a and b as an int
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return (a + b)
