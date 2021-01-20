#!/usr/bin/python3
"""Module Documentation"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Constructor method"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self):
        """Json function"""
        return self.__dict__
