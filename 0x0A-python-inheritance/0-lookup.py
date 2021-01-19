#!/usr/bin/python3
def lookup(obj):
    """Function that return the dictionary of the attributes of an object"""
    return list(dir(obj))
