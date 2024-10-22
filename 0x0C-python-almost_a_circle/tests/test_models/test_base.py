#!/usr/bin/python3
"""Unittest for Base class"""
import json
import os
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_id_auto_increment(self):
        """Test that id auto-increments when not provided"""
        Base._Base__nb_objects = 0  # Resetting the count for testing
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_given(self):
        """Test that id is correctly set when provided"""
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_id_mixed(self):
        """Test a mix of given id and auto-incremented id"""
        Base._Base__nb_objects = 0  # Resetting the count for testing
        b5 = Base()
        b6 = Base(25)
        b7 = Base()
        self.assertEqual(b5.id, 1)
        self.assertEqual(b6.id, 25)
        self.assertEqual(b7.id, 2)

    def test_to_json_string_with_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_with_empty_list(self):
        """Test to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_valid_list(self):
        """Test to_json_string with a valid list of dictionaries."""
        dict_list = [{"id": 1, "width": 10, "height": 7}]
        json_string = Base.to_json_string(dict_list)
        expected_json = json.dumps(dict_list)
        self.assertEqual(json_string, expected_json)

    def test_save_to_file_with_none(self):
        """Test save_to_file with None."""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_empty_list(self):
        """Test save_to_file with an empty list."""
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def tearDown(self):
        """Remove created files after each test."""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
