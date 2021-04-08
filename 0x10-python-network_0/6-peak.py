#!/usr/bin/python3
"""Find a peak in a unsorted list of integers"""


def find_peak(li):
    """Find a peak in a unsorted list of integers"""
    peak = []
    size = len(li)
    if li is None:
        return None
    if size == 1:
        return li[0]
    elif size == 2:
        return max(li)
    else:
        for index in range(1, size - 1):
            if li[index] >= li[index - 1] and li[index] >= li[index + 1]:
                peak.append(li[index])
        if len(peak) == 0:
            return None
        else:
            return max(peak, key=int)
