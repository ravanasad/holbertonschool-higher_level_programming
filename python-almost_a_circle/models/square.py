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

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        i = 0
        if args is not None and len(args) > 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.size = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """Return the dictionary representation of the Square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
