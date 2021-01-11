#!/usr/bin/python3
"""Module about Rectangle Class"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """Initializate a Rectangle"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @height.setter
    def height(self, value):
        """Set the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Return the area of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * self.__width) + (2 * self.__height)
