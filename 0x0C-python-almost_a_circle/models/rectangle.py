#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # area of rectangle
    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.width * self.height

    # Display # on screen
    def display(self):
        """Prints the rectangle with the character #,
        considering x and y offsets"""
        # Print y offset
        print("\n" * self.y, end="")
        # Print the rectangle with x offset
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    # overide the __str__ function
    def __str__(self):
        """Returns a string representation of the rectangle"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} "
            f"- {self.width}/{self.height}"
        )

    # update using arguments to each attributes
    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle.

        Args:
            *args (int): New attribute values.
            **kwargs (dict): New attribute values with their keys.
        """
        if args:
            # Only update attributes with args if args are provided
            attributes = ["id", "width", "height", "x", "y"]
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)

        # Skip updating with kwargs if args are provided
        elif kwargs:
            for key, value in kwargs.items():
                if key in ["id", "width", "height", "x", "y"]:
                    setattr(self, key, value)

        # return the rectangle parameters as dictionary

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
