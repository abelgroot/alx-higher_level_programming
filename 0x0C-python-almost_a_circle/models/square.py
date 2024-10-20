#!/usr/bin/python3
"""Square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): Size of the square (width and height).
            x (int): X coordinate of the square.
            y (int): Y coordinate of the square.
            id (int): ID of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    # The area and display methods are inherited from Rectangle
