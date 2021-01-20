#!/usr/bin/python3
"""Module documentation"""


def read_file(filename=""):
    """Function that read a file and print in stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
