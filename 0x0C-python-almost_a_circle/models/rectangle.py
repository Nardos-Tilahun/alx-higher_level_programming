#!/usr/bin/python3
''' Rectangle module use for define width and height'''

from models.base import Base


class Rectangle(Base):
    '''Class that inherit from the base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''getter module that return width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width module that set the width'''
        self.check_setter("width", value)
        self.__width = value

    @property
    def height(self):
        '''module that return height'''
        return self.__height

    @height.setter
    def width(self, value):
        '''module that set a value to the private member height'''
        self.check_setter("height", value)
        self.__width = value

    @property
    def x(self):
        '''getter module that return x'''
        return self.__x

    @x.setter
    def width(self, value):
        '''width module that set the x'''
        self.check_setter("x", value)
        self.__x = value

    @property
    def y(self):
        '''getter module that return y'''
        return self.__y

    @y.setter
    def width(self, value):
        '''module that set a value to the private member y'''
        self.check_setter("y", value)
        self.__y = value

    @staticmethod
    def check_setter(parameter, value):
        '''static method that valid the parameter'''

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(parameter))
        if parameter == "x" or parameter == "y":
            if value < 0:
                raise ValueError("{} must be greater than 0".format(parameter))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(parameter))

    def __str__(self):
        ''' inistane writing'''
        return "[Rectangle] {} {}/{} -{}/{}".format(self.id,
                                                    self.x,
                                                    self.y,
                                                    self.width,
                                                    self.height)

        def update(self, *args, **kwargs):
            """update the argument"""
            if args and len(args) != 0:
                a = 0
                for arg in args:
                    if a == 0:
                        if arg is None:
                            self.__init__(self.width,
                                          self.height,
                                          self.x,
                                          self.y)
                        else:
                            self.id = arg
                    elif a == 1:
                        self.width = arg
                    elif a == 2:
                        self.height = arg
                    elif a == 3:
                        self.x = arg
                    elif a == 4:
                        self.y = arg
                    a += 1
            elif kwargs and len(kwargs) != 0:
                for k, v in kwargs.items():
                    if k == "id":
                        if v is None:
                            self.__init__(self.width,
                                          self.height,
                                          self.x,
                                          self.y)
                        else:
                            self.id = v
                    elif k == "width":
                        self.width = v
                    elif k == "height":
                        self.height = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v

    def to_dictionary(self):
        """return the json in the dictionary form"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
