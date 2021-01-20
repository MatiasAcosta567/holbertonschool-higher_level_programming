#!/usr/bin/python3
"""imports"""
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""Module documentation"""


file_name = "add_item.json"
try:
    elems = load_from_json_file(file_name)
except:
    elems = []
for i in argv[1:]:
    elems.append(i)
save_to_json_file(elems, file_name)
