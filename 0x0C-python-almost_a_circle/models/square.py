#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)
        self.size = size  # This will call the setter

    @property
    def size(self):
        """Get the size of the square."""
        return self.width  # Since width == height for squares

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value  # width and height are the same
        self.height = value

    def display(self):
        """Display the square with the '#' character."""
        if self.size == 0:
            print("")  # If size is 0, just print a blank line
            return
        for i in range(self.y):
            print("")  # Print y offset
        for i in range(self.size):
            print(
                " " * self.x + "#" * self.size
            )  # Print x offset followed by the square

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
