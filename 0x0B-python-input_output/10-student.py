#!/usr/bin/python3
"""Module that defines a class Student by: (based on 9-student.py)"""


class Student:
    """
    Defines a student

    Atrributes:
        first_name: The first name of the student
        last_name: The last name of the student
        age: The age of the student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize the student

        Args:
            first_name: The first name of the student
            last_name: The last name of the student
            age: The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__

        value = {}
        for a in attrs:
            if a in self.__dict__:
                value.append(self.__dict__[a])
        my_dict = {}
        for i in range(0, len(attrs)):
            my_dict.append("'{}': '{}'".format(attrs[i], value[i]))
        return my_dict
