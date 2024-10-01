#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that defines a square by size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiate a square with a given size and position."""
        self.size = size  # Use the setter to set the size
        self.position = position  # Use the setter to set the position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position  # Return the private attribute

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or any(i < 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Set the private attribute

    def area(self):
        """Return the current square area."""
        return self.__size**2  # Area of the square

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print("")  # Print an empty line if size is 0
            return

        # Print the square at the specified position
        print(
            "\n" * self.__position[1], end=""
        )  # Print new lines for vertical position
        for _ in range(self.__size):
            print(
                " " * self.__position[0] + "#" * self.__size
            )  # Print each row of the square
