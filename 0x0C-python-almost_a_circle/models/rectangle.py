#!/usr/bin/python3
"""Module for Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle is a class that inherits from Base and defines a rectangle

    Attributes:
        width: its width
        height: its height
        x, y: describe the position of the rectangle
        id: its id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Inititialize the rectangle object

        Args:
            width: its width
            height: its height
            x, y: describe the position of the rectangle
            id: the id of the object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter

        Args:
            value: the value of the width as an int and > 0
        """
        self.int_validator("width", value, 0)
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter

        Args:
            value: the value of the height as an int and > 0
        """
        self.int_validator("height", value, 0)
        self.__height = value

    @property
    def x(self):
        """Returns the x position(space before the rectangle, form the left)"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter

        Args:
            value: the value of x as an int and >= 0
        """
        self.int_validator("x", value, 1)
        self.__x = value

    @property
    def y(self):
        """Returns the y positon(space before the rectangle, from the top)"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter

        Args:
            value: the value of y as an int and >= 0
        """
        self.int_validator("y", value, 1)
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the Rectangle with the character # """
        y = "\n" * self.__y
        rect = " " * self.__x
        rect += "#" * self.__width
        rect += "\n"
        rect *= self.__height
        print("{}{}".format(y, rect), end="")

    def __str__(self):
        """Returns the characteristic of the rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        update the rectangle

        Args:
            1st: id attribute
            2nd: width attribute
            3rd: height attribute
            4th: x attribute
            5th: y attribute
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        the_dict = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
        return the_dict
