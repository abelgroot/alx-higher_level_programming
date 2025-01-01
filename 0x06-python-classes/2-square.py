#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that defines a square by size."""

    def __init__(self, size=0):
        """Instantiate a square with a given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size  # Private attribute
