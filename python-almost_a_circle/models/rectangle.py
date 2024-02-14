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

    def area(self):
        """Calculate the area of rectangle and then return"""
        return self.__width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        for i in range(0, self.y):
            print()
        for i in range(0, self.__height):
            for _ in range(0, self.x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        str1 = f"[Rectangle] ({self.id}) {self.x}/"
        str2 = f"{self.y} - {self.width}/{self.height}"
        return str1 + str2

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        i = 0
        if args is not None and len(args) > 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.width = kwargs[key]
                elif key == "height":
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
