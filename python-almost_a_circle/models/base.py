#!/usr/bin/python3
"""
This module defines a class for a Base
"""


import json


class Base:
    """Defines a base object.
    Attributes:
        id (int): id of base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(ld):
        """returns the JSON string representation of list_dictionaries"""
        if ld is None or len(ld) == 0:
            return "[]"
        return json.dumps(ld)

    def from_json_string(js):
        """returns the list of the JSON string representation json_string"""
        if js is None or len(js) == 0:
            return []
        return json.loads(js)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                obj = cls(10, 10)
            else:
                obj = cls(10)
        obj.update(**dictionary)
        return obj
