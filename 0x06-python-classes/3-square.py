#!/usr/bin/python3
""" This is a module to do size validation of Square Class"""


class Square:
    """ This is a square class that has
            an attribute of size (Private Instance)
            it checks the size type and value"""
    def __init__(self, size=0):
        """ This is to create initalization for size"""
        self.siz = size

    @property
    def siz(self):
        """ This is a getter for the size"""
        return self.__size

    @siz.setter
    def siz(self, value):
        """ This is a setter fot the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """ This will calulate the area of the Square"""
        return self.siz**2
