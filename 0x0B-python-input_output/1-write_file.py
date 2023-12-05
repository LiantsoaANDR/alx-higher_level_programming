#!/usr/bin/python3
"""Module for writing a string in a file"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)

    Args:
        filename: the file to write into
        text: the text to write into the file

    Return: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
