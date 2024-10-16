#!/usr/bin/python3
"""
This module provides a function that reads a text file (UTF8)
and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to be read. Default is an empty string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
