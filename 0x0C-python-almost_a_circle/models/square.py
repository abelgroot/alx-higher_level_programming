#!/usr/bin/python3
"""Defines a square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the new square.
            x (int): The x-coordinate of the new square.
            y (int): The y-coordinate of the new square.
            id (int): The identity of the new square.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to set for the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is <= 0.
        """
        self.width = value
        self.height = value

    def display(self):
        """Print the square using the `#` character."""
        if self.size == 0:
            print("")  # Blank line if size is 0
            return
        for _ in range(self.y):
            print("")
        for _ in range(self.size):
            print(" " * self.x + "#" * self.size)

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Assign attributes based on the order of *args or **kwargs.

        Args:
            *args: Non-keyword arguments.
                1st argument -> id attribute
                2nd argument -> size attribute
                3rd argument -> x attribute
                4th argument -> y attribute
            **kwargs: Keyword arguments representing attribute key-value pairs.
        """
        if args:
            # Only update attributes with args if args are provided
            attributes = ["id", "size", "x", "y"]
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)

        # Skip updating with kwargs if args are provided
        elif kwargs:
            for key, value in kwargs.items():
                if key in ["id", "size", "x", "y"]:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
