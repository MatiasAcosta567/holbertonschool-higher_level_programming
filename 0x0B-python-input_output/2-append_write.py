#!/usr/bin/python3
"""Module Documentation"""


def append_write(filename="", text=""):
    """Function that append a text """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
