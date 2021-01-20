#!/usr/bin/python3
"""imports"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""Module documentation"""

try:
    elems = load_from_json_file("add_item.json")
except:
    elems = []
for i in argv[1:]:
    elems.append(i)
save_to_json_file(elems, "add_item.json")
