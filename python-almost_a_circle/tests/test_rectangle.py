#!/usr/bin/python3

"""
    This module defines a Test class for a Rectangle
"""


import unittest


from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.height, 2)

    def test_rectangle_2(self):
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.x, 3)

    def test_rectangle_3(self):
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.y, 4)

    def test_rectangle_4(self):
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)

    def test_rectangle_type_error_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_rectangle_type_error_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_rectangle_type_error_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
    
    def test_rectangle_type_error_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")
    
    def test_rectangle_value_error_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_rectangle_value_error_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)
    
    def test_rectangle_value_error_width_2(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_rectangle_value_error_height_2(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_rectangle_value_error_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_rectangle_value_error_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
    
    def test_display(self):
        r1 = Rectangle(2, 2, 0, 0, 0)
        self.assertEqual(r1.display(), "##\n##\n")

    def test_display_without_x_y(self):
        r1 = Rectangle(2, 2)
        self.assertEqual(r1.display(), "##\n##\n")

    def test_display_witho_y(self):
        r1 = Rectangle(2, 2, 1)
        self.assertEqual(r1.display(), " ##\n ##\n")

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
    
    def test_update_2(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 1)
        self.assertEqual(r1.width, 1)

    def test_update_3(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 1, 2)
        self.assertEqual(r1.height, 2)

    def test_update_4(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 1, 2, 3)
        self.assertEqual(r1.x, 3)

    def test_update_5(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 1, 2, 3, 4)
        self.assertEqual(r1.y, 4)

    def test_update_6(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(**{'id': 89})
        self.assertEqual(r1.id, 89)
    
    def test_update_7(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(**{'id': 89, 'width': 1})
        self.assertEqual(r1.width, 1)
    
    def test_update_8(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r1.height, 2)

    def test_update_9(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r1.x, 3)

    def test_update_10(self):
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
    
    def save_to_file_none(self):
        Rectangle.save_to_file(None)
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output, [])

    def save_to_file_empty(self):
        Rectangle.save_to_file([])
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output, [])

    def test_load_from_file(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        list_input = [r1, r1, r1]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output[0].id, 10)

    def test_load_from_file_when_file_does_not_exist(self):
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output, [])

if __name__ == "__main__":
    unittest.main()