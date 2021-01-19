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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
