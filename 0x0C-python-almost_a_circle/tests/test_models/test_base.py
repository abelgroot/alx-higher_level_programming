#!/usr/bin/python3
"""Unittest for Base class"""
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def setUp(self):
        """Reset nb_objects before each test"""
        Base._Base__nb_objects = 0  # Resetting the count for testing

    def test_base_initialization(self):
        """Test initialization of Base instances"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)  # Should be the next id after 2


if __name__ == "__main__":
    unittest.main()
