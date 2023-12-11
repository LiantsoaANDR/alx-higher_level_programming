#!/usr/bin/python3
"""Defines unittests for base.py"""
import unittest
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class Test_Base(unittest.TestCase):
    """Unittest for testing the Base class"""
    def setUp(self):
        """putting the counter of objects to 0 before testing"""
        Base._Base__nb_objects = 0

    def test_to_json_string(self):
        """Test the to_json_string method"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        json_result = Base.to_json_string([r1.to_dictionary(),
                                           r2.to_dictionary()])
        self.assertEqual(json_result, '[{
                                            "id": 5, "width": 1,
                                            "height": 2, "x": 3,
                                            "y": 4
                                        }, {
                                                "id": 10,
                                                "width": 6,
                                                "height": 7,
                                                "x": 8,
                                                "y": 9
                                            }]')

    def test_save_to_file(self):
        """test the save_to_file method"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertEqual(content, '[{
                                            "id": 5,
                                            "width": 1,
                                            "height": 2,
                                            "x": 3, "y": 4
                                        }, {
                                                "id": 10,
                                                "width": 6,
                                                "height": 7,
                                                "x": 8,
                                                "y": 9
                                            }]')

    def test_from_json_string(self):
        """Test the from_json_strin method"""
        json_string = '[{
                                "id": 5,
                                "width": 1,
                                "height": 2,
                                "x": 3, "y": 4
                            }, {
                                    "id": 10,
                                    "width": 6,
                                    "height": 7,
                                    "x": 8,
                                    "y": 9
                                }]'
        json_result = Base.from_json_string(json_string)
        self.assertEqual(json_result, [{
                                            "id": 5,
                                            "width": 1,
                                            "height": 2,
                                            "x": 3,
                                            "y": 4
                                        }, {
                                                "id": 10,
                                                "width": 6,
                                                "height": 7,
                                                "x": 8,
                                                "y": 9
                                            }])

    def test_create(self):
        """Test the create method"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1_dict = r1.to_dictionary()
        self.assertEqual(new_instance.__str__(), '[Rectangle] (5) 3/4 - 1/2')


if __name__ == '__main__':
    unittest.main()
