#!/usr/bin/python3
"""Square class with size attribute"""


class Square:
    """Square class with size attribute"""
    def __init__(self, size=0, position=(0,0)):
        """Initializes the Square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size;
        self.__position = position;

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)

    @property
    def position(self):
        """Returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
