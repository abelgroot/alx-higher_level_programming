#!/usr/bin/python3
"""
Module defining the Student class.
"""


class Student:
    """
    A class to define a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary representation of the student.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
        }
