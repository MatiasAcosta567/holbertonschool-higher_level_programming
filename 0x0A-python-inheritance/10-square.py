#!/usr/bin/python3
"""Module of geometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
    """Square class"""

    def __init__(self, size):
        """Constructor method"""
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self,size, size)

    def area(self):
        """Area method"""
        return super().area()

    def __str__(self):
        """String method"""
        return super().__str__()

