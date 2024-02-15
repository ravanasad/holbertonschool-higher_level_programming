#!/usr/bin/python3
"""
This module defines a class for a Base
"""


import json
import os


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
        if js is None or js == "[]":
            return []
        return json.loads(js)

    @classmethod
    def save_to_file(cls, list_input):
        """Save list input to file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as newfile:
            if list_input is None:
                result = "[]"
            else:
                dic = [v_input.to_dictionary() for v_input in list_input]
                result = Base.to_json_string(dic)
            newfile.write(result)

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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as newfile:
                mylist = Base.from_json_string(newfile.read())
                result = [cls.create(**dic) for dic in mylist]
                return result
        except IOError:
            return []
