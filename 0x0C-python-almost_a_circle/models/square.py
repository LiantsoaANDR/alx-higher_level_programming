#!/usr/bin/python3
"""Module for Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square is a class that inherits from Rectangle and defines a Square

    Attributes:
        size: the size of the square
        x, y: describe the position of the square
        id: its id
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the square object

        Args:
            size: its size
            x, y: describe its position
            id: its id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the characteristic of the square"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Return the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter

        Args:
            value: the value of the size as an int and > 0
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update the square

        Args:
            *args: list of arguments
                1st: id attribute
                2nd: size attribute
                3th: x attribute
                4th: y attribute
            **kwargs: can be thought of as a double pointer to a dictionary:
                      key/value(keyworded arguments)
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                    continue
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        the_dict = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return the_dict
