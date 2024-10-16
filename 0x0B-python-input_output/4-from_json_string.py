#!/usr/bin/python3
"""
This module defines a function that converts a JSON string
to a Python object (data structure).
"""

import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python object represented by the JSON string.
    """
    return json.loads(my_str)
