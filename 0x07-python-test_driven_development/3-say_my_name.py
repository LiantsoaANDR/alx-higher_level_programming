#!/usr/bin/python3
""" Module for printing first and last name """


def say_my_name(first_name, last_name=""):
    """
    Prints: My name is <first name> <last name>

    args:
        first_name: the first to print
        last_name: the last name to print
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
