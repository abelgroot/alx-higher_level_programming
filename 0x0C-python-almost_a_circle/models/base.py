#!/usr/bin/python3
"""Base class module"""
import json


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
