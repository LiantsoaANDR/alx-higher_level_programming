#!/usr/bin/python3
"""Module to append a sting at the end of a file"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)

    Args:
        filename: the name of the file
        text: the text to put into the end of filename

    Return: the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
