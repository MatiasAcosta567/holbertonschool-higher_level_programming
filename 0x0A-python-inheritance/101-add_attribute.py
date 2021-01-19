#!/usr/bin/python3
def add_attribute(obj, field, value):
    if hasattr(obj, field):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, field, value)
