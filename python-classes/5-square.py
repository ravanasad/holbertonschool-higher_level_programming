#!/usr/bin/python3
"""Square class with size attribute"""
class Square:
    """Square class with size attribute"""
    def __init__(self, size=0):
        """Initializes the Square class"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

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
