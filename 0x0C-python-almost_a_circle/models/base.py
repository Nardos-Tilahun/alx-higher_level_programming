#!/usr/bin/python3
''' how to create a base class'''

class Base():
    ''' Assign Id for the instances of the class'''
    __nb_objects = 0;
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
