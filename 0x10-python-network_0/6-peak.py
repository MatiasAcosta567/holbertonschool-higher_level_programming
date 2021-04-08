#!/usr/bin/python3
"""Find a peak in a unsorted list of integers"""


def find_peak(list_integers):
    """Find a peak in a unsorted list of integers"""
    if list_integers == []:
        return None

    size = len(list_integers)
    if size == 1:
        return list_integers[0]
    elif size == 2:
        return max(list_integers)

    middle = int(size / 2)
    peak = list_integers[middle]
    if peak > list_integers[middle - 1] and peak > list_integers[middle + 1]:
        return peak
    elif peak < list_integers[middle - 1]:
        return find_peak(list_integers[:middle])
    else:
        return find_peak(list_integers[middle + 1:])
