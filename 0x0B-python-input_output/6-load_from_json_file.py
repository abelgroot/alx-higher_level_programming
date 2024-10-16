#!/usr/bin/python3
"""
This module defines a function to create an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        The object represented by the JSON string in the file.
    """
    with open(filename, "r") as f:
        return json.load(f)
