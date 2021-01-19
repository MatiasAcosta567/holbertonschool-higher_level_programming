#!/usr/bin/python3
"""Module documentation"""


def inherits_from(obj, a_class):
    """Function documentation"""
    if issubclass(type(obj), a_class):
        if type(obj) == a_class:
            return False
        else:
            return True
    else:
        return False
