#!/usr/bin/python3
"""Class inherit of a list"""


class MyList(list):
    """Class inherit from a list"""
    def print_sorted(self):
        print(sorted(self))
