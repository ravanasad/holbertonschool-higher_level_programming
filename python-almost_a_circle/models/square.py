#!/usr/bin/python3
"""
    This module defines a class for a rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines an object for a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height
        attr:
            width, height, x and y
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
