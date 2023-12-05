#!/usr/bin/python3
"""Module that defines a class Student"""


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

    def to_json(self):
        """returns a dictionary representation of a Student instance"""
        return self.__dict__
