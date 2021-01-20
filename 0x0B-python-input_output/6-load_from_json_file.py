#!/usr/bin/python3
"""Function that creates an Object from a JSON file"""


import json

def load_from_json_file(filename):
    """function that create an object from a json file"""


    with open(filename, encoding="utf-8") as f:
        return json.load(f)
