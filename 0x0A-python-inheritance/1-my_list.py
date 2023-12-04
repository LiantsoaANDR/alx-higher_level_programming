#!/usr/bin/python3
"""module for a class that inherits from list"""


class MyList(list):
    """ A list class """

    def print_sorted(self):
        """  prints the list, but sorted (ascending sort) """
        print (sorted(self))
