#!/usr/bin/python3
"""
This module contains the function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited (directly
    or indirectly) from the specified class. Otherwise returns False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
