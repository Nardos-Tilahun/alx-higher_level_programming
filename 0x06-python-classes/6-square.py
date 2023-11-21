#!/usr/bin/python3
""" This is a module to do size validation of Square Class"""


class Square:
    """ This is a square class that has
            an attribute of size (Private Instance)
            it checks the size type and value"""
    def __init__(self, size=0, position=(0, 0)):
        """ This is to create initalization for size"""
        self.__size = size
        self.__position = position

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
        if (isinstance(value, tuple) and len(value) == 2 and \
                (isinstance(i, int) and i >= 0  for i in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ This will calulate the area of the Square"""
        return self.__size**2

    def my_print(self):
        """ This is to print the squares to the stdout"""
        for i in range(0, self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
