#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines a class for testing max_integer function"""
    def test_list(self):
        """Test for list of integers"""
        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)

    def test_empty_list(self):
        """Test for empty list"""
        list = []
        self.assertEqual(max_integer(list), None)

    def test_negative_numbers(self):
        """Test for negative numbers"""
        list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list), -1)


if __name__ == '__main__':
    unittest.main()
