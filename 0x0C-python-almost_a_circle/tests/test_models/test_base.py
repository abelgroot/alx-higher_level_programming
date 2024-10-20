#!/usr/bin/python3
"""Unittest for Base class"""
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


if __name__ == "__main__":
    unittest.main()
