#!/usr/bin/python3
import json
"""Module documentation"""


def load_from_json_file(filename):
    """function that create an object from a json file"""
    with open(filename, mode="r") as f:
        return json.load(f)
