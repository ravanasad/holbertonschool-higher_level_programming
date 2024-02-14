#!/usr/bin/python3
"""
    This module defines a class for a rectangle
"""


from models.base import Base


class Rectangle(Base):
    """This class defines an object for a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        width, height, x and y
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        elif value <= 0:
            raise ValueError(f"width must be > 0")
        self.__width = value
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        elif value <= 0:
            raise ValueError(f"height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError(f"x must be an integer")
        elif value < 0:
            raise ValueError(f"x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError(f"y must be an integer")
        elif value < 0:
            raise ValueError(f"y must be >= 0")
        self.__y = value
