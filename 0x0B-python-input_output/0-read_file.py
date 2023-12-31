#!/usr/bin/python3
"""Module for reading a file"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: the file to read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
