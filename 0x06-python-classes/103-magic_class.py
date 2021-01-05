#!/usr/bin/python3
"""Magic module"""

class MagicClass:
    """Magic Class"""
    def __init__(self, radius):
        """Constructor method"""
        if type(radius) != int or type(radius) != float:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """return the area of a circle"""
        return (self.radius ** 2) * math.pi

    def circumference:
        """retutrn a circumference of a circle"""
        return (2 * math.pi) * self.radius
