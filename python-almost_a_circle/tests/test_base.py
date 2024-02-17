#!/usr/bin/python3

"""
    This module defines a Test class for a Base
"""


import unittest


from models.base import Base


class TestBase(unittest.TestCase):
    
    def test_id_1(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
    
    def test_to_json_string_without_arg(self):
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_with_arg(self):
        json_dictionary = Base.to_json_string([{'id': 89}])
        self.assertEqual(json_dictionary, '[{"id": 89}]')

    def test_to_json_string_with_none(self):
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")
    
    def test_from_json_string_empty(self):
        json_dictionary = Base.from_json_string("[]")
        self.assertEqual(json_dictionary, [])

    def test_from_json_string(self):
        json_dictionary = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(json_dictionary, [{'id': 89}])

if __name__ == "__main__":
    unittest.main()
    

    


