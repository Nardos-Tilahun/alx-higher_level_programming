#!/usr/bin/python3
""" This is a module to do size validation of Square Class"""


class Square:
    """ This is a square class that has
            an attribute of size (Private Instance)
            it checks the size type and value"""
    def __init__(self, size=0, position=(0, 0)):
        """ This is to create initalization for size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """ This is a getter for the size"""
        return self.__size

    @property
    def position(self):
        """ This is a method to get the postion """
        return self.__position

    @size.setter
    def size(self, value):
        """ This is a setter fot the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ This is to check the position is valid and set to attribute"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ This will calulate the area of the Square"""
        return self.__size**2

    def my_print(self):
        """ This is to print the squares to the stdout"""
        if self.__size == 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for j in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
