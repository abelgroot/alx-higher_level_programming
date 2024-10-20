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

    def test_invalid_width(self):
        """Test invalid width values"""
        with self.assertRaises(TypeError) as cm:
            Rectangle("10", 2)
        self.assertEqual(str(cm.exception), "width must be an integer")

        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as cm:
            r.width = -10
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_invalid_height(self):
        """Test invalid height values"""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")

        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as cm:
            r.height = 0
        self.assertEqual(str(cm.exception), "height must be > 0")

    def test_invalid_x(self):
        """Test invalid x values"""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, "3")
        self.assertEqual(str(cm.exception), "x must be an integer")

        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as cm:
            r.x = -1
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_invalid_y(self):
        """Test invalid y values"""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 3, "4")
        self.assertEqual(str(cm.exception), "y must be an integer")

        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as cm:
            r.y = -1
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_area_of_rectangle(self):
        """Test area of a rectangle"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)


if __name__ == "__main__":
    unittest.main()
