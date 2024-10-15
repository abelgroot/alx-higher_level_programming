#!/usr/bin/python3
"""
This module defines a function that checks
if an object is an exact instance of a class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class
    Otherwise, returns False
    """
    return type(obj) is a_class
