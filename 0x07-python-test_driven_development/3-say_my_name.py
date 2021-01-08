#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if type(first_name) != string:
        raise TypeError("first_name must be a string")
    elif type(last_name) != string:
        raise TypeError("last_name must be a string")
    else:
        return "My name is {} {}".format(first_name, last_name)
