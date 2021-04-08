#!/usr/bin/python3
"""Find a peak in a unsorted list of integers"""


def find_peak(li):
    """Find a peak in a unsorted list of integers"""
    peak = []
    for index in range(1, len(li) - 1):
        if li[index] >= li[index - 1] and li[index] >= li[index + 1]:
            peak.append(li[index])
    if len(peak) == 0:
        return None
    else:
        return max(peak, key=int)
