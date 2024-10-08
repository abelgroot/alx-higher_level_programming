#!/usr/bin/python3
"""
This module defines a class Rectangle with private instance attributes
width and height, and provides getters and setters for them.
"""


class Rectangle:
    """
    This class defines a rectangle with private attributes width and height,
    and contains property setters and getters to manage these attributes.
    """

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle,
        ensuring it is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle,
        ensuring it is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
