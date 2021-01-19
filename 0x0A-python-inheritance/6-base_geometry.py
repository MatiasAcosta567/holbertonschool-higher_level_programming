#!/usr/bin/python3
"""Module of geometry"""


class BaseGeometry:
    """Class about base geometry"""

    def area(self):
        """Calculate area of geometry"""
        raise Exception("area() is not implemented")
