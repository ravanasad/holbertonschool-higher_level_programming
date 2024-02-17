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


class TestRectangle(unittest.TestCase):

    def test_rectangle(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.x, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.y, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)
    
    def test_rectangle_errors(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
    
    def test_display(self):
        r0 = Rectangle(2, 5)
        with patch("sys.stdout", new=StringIO()) as output:
            r0.display()
            self.assertEqual(output.getvalue(), "##\n##\n##\n##\n##\n")
        r1 = Rectangle(2, 2, 2)
        with patch("sys.stdout", new=StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue(), '  ##\n  ##\n')
        r2 = Rectangle(2, 2, 2, 2)
        with patch("sys.stdout", new=StringIO()) as output:
            r2.display()
            self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n") 

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
    
    def test_to_dictionary(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.to_dictionary(), {'x': 2, 'y': 1, 'id': 12,
                    'height': 6, 'width': 4})
        
    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 1)
        self.assertEqual(r1.width, 1)
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 1, 2)
        self.assertEqual(r1.height, 2)
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 1, 2, 3)
        self.assertEqual(r1.x, 3)
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 1, 2, 3, 4)
        self.assertEqual(r1.y, 4)
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(**{'id': 89})
        self.assertEqual(r1.id, 89)
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(**{'id': 89, 'width': 1})
        self.assertEqual(r1.width, 1)
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r1.height, 2)
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r1.x, 3)
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r1.y, 4)
    
    def test_create(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r2 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r2.id, 89)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

    def test_load_from_file(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r2 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        r3 = Rectangle.create(**{'id': 90, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        r4 = Rectangle.create(**{'id': 91, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        list_input = [r2, r3, r4]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output[0].id, 89)
        self.assertEqual(list_output[1].id, 90)
        self.assertEqual(list_output[2].id, 91)
    
    def test_save_to_file_none(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as output:
            self.assertEqual(output.read(), "[]")
        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as output:
            self.assertEqual(output.read(), '[]')

    def test_load_from_file(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        list_input = [r1, r1, r1]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output[0].id, 10)

    def test_load_from_file_when_file_does_not_exist(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

if __name__ == "__main__":
    unittest.main()