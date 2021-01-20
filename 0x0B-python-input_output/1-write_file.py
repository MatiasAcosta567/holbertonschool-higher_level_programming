#!/usr/bin/python3
"""Module Documentation"""


def write_file(filename="", text=""):
    """Function that write text in a file"""
    with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(text)

