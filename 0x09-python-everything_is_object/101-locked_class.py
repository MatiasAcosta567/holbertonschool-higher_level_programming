#!/usr/bin/python3
"""Module about locked Class"""


class LockedClass():
    """A class that control que puede tener the class and don't
        permite create other methods or attributes"""
    __slots__ = "first_name"
