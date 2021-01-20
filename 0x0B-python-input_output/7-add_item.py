#!/usr/bin/python3
import json
from sys import argv
import os
"""Module documentation"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if len(argv) > 1:
    elems = []
    file_name = "add_item.json"
    if os.path.exists(file_name):
        file_list = load_from_json_file(file_name)
        for elements in file_list:
            elems.append(elements)
    for i in range(1, len(argv)):
        elems.append(argv[i])
    save_to_json_file(elems, file_name)
