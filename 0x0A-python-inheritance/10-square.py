#!/usr/bin/python3
"""This module defines a Square class that inherits from Rectangle."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class used to represent a square."""

    def __init__(self, size):
        """
        Initialize the square with size.

        Args:
            size (int): The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size**2
