#!/usr/bin/python3
"""Define a Square Class"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Constructor method"""
        try:
            int(size)
            if (size < 0):
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
