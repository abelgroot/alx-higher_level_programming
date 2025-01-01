#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that defines a square by size."""

    def __init__(self, size=0):
        """Instantiate a square with a given size."""
        self.size = size  # Use the setter to set the size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size  # Return the private attribute

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Set the private attribute

    def area(self):
        """Return the current square area."""
        return self.__size**2  # Area of the square
