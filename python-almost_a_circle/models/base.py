#!/usr/bin/python3
"""
This module defines a class for a Base
"""
class Base:
    """Defines a base object.

    Attributes:
        id (int): id of base
    """
    __nb_objects  = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

