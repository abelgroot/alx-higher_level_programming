#!/usr/bin/python3
"""Base class module"""
import csv
import json
import os
import turtle


class Base:
    """Base class to manage 'id' attribute across future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor that handles 'id' management"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        If list_dictionaries is None or empty, returns the string "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        The file name is <Class name>.json.
        """
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        with open(filename, "w") as f:
            # Convert the list of objects to a list of dictionaries
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_dicts)
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            dictionary (dict): A dictionary of attributes.

        Returns:
            Instance of Rectangle or Square with attributes set.
        """
        # Deferred import to avoid circular dependency
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            # Create a dummy Rectangle instance
            dummy = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            # Create a dummy Square instance
            dummy = Square(1)  # Using default value for dummy size

        # Use update method to assign attributes from dictionary
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file.

        If the file doesn't exist, returns an empty list.
        Otherwise, returns a list of instances of the current class.
        """
        filename = f"{cls.__name__}.json"

        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            json_string = file.read()

        list_dictionaries = cls.from_json_string(json_string)
        instances = [cls.create(**d) for d in list_dictionaries]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to CSV and saves it to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([
                        obj.id, obj.width, obj.height, obj.x, obj.y
                    ])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV and returns a list of instances."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                list_objs = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls.create(
                            id=int(row[0]),
                            width=int(row[1]),
                            height=int(row[2]),
                            x=int(row[3]),
                            y=int(row[4]),
                        )
                    elif cls.__name__ == "Square":
                        obj = cls.create(
                            id=int(row[0]),
                            size=int(row[1]),
                            x=int(row[2]),
                            y=int(row[3]),
                        )
                    list_objs.append(obj)
                return list_objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Rectangles and Squares using the turtle module."""
        screen = turtle.Screen()
        screen.bgcolor("white")
        t = turtle.Turtle()
        t.shape("turtle")
        t.speed(3)  # Slow speed for animation

        # Function to draw a rectangle
        def draw_rectangle(t, width, height, x, y):
            """Draw a rectangle with turtle."""
            t.penup()
            t.goto(x, y)  # Go to the specified starting position
            t.pendown()
            for _ in range(2):
                t.forward(width)
                t.left(90)
                t.forward(height)
                t.left(90)

        # Function to draw a square
        def draw_square(t, size, x, y):
            """Draw a square with turtle."""
            draw_rectangle(t, size, size, x, y)

        # Draw all rectangles
        t.color("blue")
        for rect in list_rectangles:
            draw_rectangle(t, rect.width, rect.height, rect.x, rect.y)

        # Draw all squares
        t.color("green")
        for sqr in list_squares:
            draw_square(t, sqr.size, sqr.x, sqr.y)

        # Hide the turtle and finish the drawing
        t.hideturtle()
        turtle.done()
