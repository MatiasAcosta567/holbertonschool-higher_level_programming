#!/usr/bin/python3
"""Module documentation"""


def is_same_class(obj, a_class):
    """compare if 2 an object is an instance"""
    if obj.__class__ == a_class:
        return True
    else:
        return False
