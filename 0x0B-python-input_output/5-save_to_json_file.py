#!/usr/bin/python3
import json
"""Module documentation"""


def save_to_json_file(my_obj, filename):
    """function that convert json obj to file"""
    with open(filename, mode="w", encoding="utf-8") as f:
            f.write(json.dumps(my_obj))
