#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class"""

    def setUp(self):
        """Reset nb_objects before each test"""
        Base._Base__nb_objects = 0  # Resetting the count for testing

    def test_rectangle_initialization(self):
        """Test initialization of Rectangle instances"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)  # Should now be 1

        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 2)  # Should now be 2

        self.assertEqual(r3.id, 12)  # id provided should be 12
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)


if __name__ == "__main__":
    unittest.main()
