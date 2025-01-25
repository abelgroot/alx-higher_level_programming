#!/usr/bin/python3
"""Module to find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a peak element in a list of unsorted integers.
    A peak is an element that is greater than or equal to its neighbors.
    """
    if not list_of_integers:
        return None

    start, end = 0, len(list_of_integers) - 1

    while start < end:
        mid = (start + end) // 2

        # Compare mid with its neighbors
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            end = mid

    return list_of_integers[start]
