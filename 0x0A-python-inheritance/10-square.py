#!/usr/bin/python3
"""Module of geometry"""


class BaseGeometry:
    """Class about base geometry"""

    def area(self):
        """Calculate area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validator of integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle inherited of base geometry"""

    def __init__(self, width, height):
        """Constructor method"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()

    def __str__(self):
        return super().__str__()
