#!/usr/bin/python3
"""Function that writes an Object to text file, using a JSON representation """


import json


def save_to_json_file(my_obj, filename):
    """function that convert json obj to file"""


    with open(filename, mode="w", encoding="utf-8") as f:
            f.write(json.dumps(my_obj))
