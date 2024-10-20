#!/usr/bin/python3
"""Base class module"""


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
