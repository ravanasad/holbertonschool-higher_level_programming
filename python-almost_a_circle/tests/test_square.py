#!/usr/bin/python3

"""
    This module defines a Test class for a Rectangle
"""


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square(self):
        test = Square(5)
        self.assertEqual(test.size, 5)
        test = Square(5, 10)
        self.assertEqual(test.x, 10)
        test = Square(5, 10, 15)
        self.assertEqual(test.y, 15)
        test = Square(5, 10, 15, 20)
        self.assertEqual(test.id, 20)
    
    def test_square_error(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "10")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, "15")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 10, -15)
        
    def test_area(self):
        test = Square(5)
        self.assertEqual(test.area(), 25)

    def test_display(self):
        test = Square(2, 2, 2)
        with patch("sys.stdout", new=StringIO()) as output:
            test.display()
            self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n")
        test = Square(2, 2)
        with patch("sys.stdout", new=StringIO()) as output:
            test.display()
            self.assertEqual(output.getvalue(), "  ##\n  ##\n")
    
    def test_str(self):
        test = Square(5, 10, 15, 20)
        self.assertEqual(test.__str__(), "[Square] (20) 10/15 - 5")

    def test_update(self):
        test = Square(1, 2, 3, 4)
        test.update(1)
        self.assertEqual(test.id, 1)
        test.update(1, 2)
        self.assertEqual(test.size, 2)
        test.update(1, 2, 3)
        self.assertEqual(test.x, 3)
        test.update(1, 2, 3, 4)
        self.assertEqual(test.y, 4)
        test.update(1, 2, 3, 4)
        self.assertEqual(test.id, 1)

    def test_create(self):
        test = Square(5, 10, 15, 20)
        test_dictionary = test.to_dictionary()
        test2 = Square.create(**test_dictionary)
        self.assertEqual(test.__str__(), test2.__str__())

    def test_save_to_file(self):
        test = Square(5, 10, 15, 20)
        test2 = Square(10, 20, 30, 40)
        Square.save_to_file([test, test2])
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

    def test_load_from_file(self):
        test = Square(5, 10, 15, 20)
        test2 = Square(10, 20, 30, 40)
        Square.save_to_file([test, test2])
        list_objs = Square.load_from_file()
        self.assertEqual(list_objs[0].__str__(), test.__str__())
        self.assertEqual(list_objs[1].__str__(), test2.__str__())
        os.remove("Square.json")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

    def test_load_from_file_empty(self):
        list_objs = Square.load_from_file()
        self.assertEqual(list_objs, [])