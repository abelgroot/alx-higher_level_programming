#!/usr/bin/python3
"""Unittest for Rectangle class"""
import sys
import unittest
from io import StringIO

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

    def test_area(self):
        """Test area of a rectangle"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test the display method of Rectangle"""
        r1 = Rectangle(4, 3, 2, 1)
        expected_output = "\n  ####\n  ####\n  ####\n"
        
        # Capture the output of the display method
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__  # Reset redirect.
        
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_with_no_offset(self):
        """Test the display method with no x and y offsets"""
        r2 = Rectangle(3, 2, 0, 0)
        expected_output = "###\n###\n"
        
        # Capture the output of the display method
        captured_output = StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__  # Reset redirect.
        
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_with_only_y_offset(self):
        """Test the display method with only y offset"""
        r3 = Rectangle(5, 4, 0, 2)
        expected_output = "\n\n#####\n#####\n#####\n#####\n"

        # Capture the output of the display method
        captured_output = StringIO()
        sys.stdout = captured_output
        r3.display()
        sys.stdout = sys.__stdout__  # Reset redirect.

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_with_only_x_offset(self):
        """Test the display method with only x offset"""
        r4 = Rectangle(2, 2, 3, 0)
        expected_output = "   ##\n   ##\n"

        # Capture the output of the display method
        captured_output = StringIO()
        sys.stdout = captured_output
        r4.display()
        sys.stdout = sys.__stdout__  # Reset redirect.

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update_id(self):
        """Test updating the id of the Rectangle."""
        r1 = Rectangle(10, 2)
        r1.update(89)
        self.assertEqual(r1.id, 89)

    def test_update_width(self):
        """Test updating the width of the Rectangle."""
        r1 = Rectangle(10, 2)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)

    def test_update_height(self):
        """Test updating the height of the Rectangle."""
        r1 = Rectangle(10, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)

    def test_update_x(self):
        """Test updating the x attribute of the Rectangle."""
        r1 = Rectangle(10, 2)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)

    def test_update_y(self):
        """Test updating the y attribute of the Rectangle."""
        r1 = Rectangle(10, 2)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_update_multiple_attributes(self):
        """Test updating multiple attributes at once."""
        r1 = Rectangle(10, 2)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_update_no_args(self):
        """Test that no arguments do not change attributes."""
        r1 = Rectangle(10, 2)
        original_id = r1.id
        original_width = r1.width
        original_height = r1.height
        original_x = r1.x
        original_y = r1.y
        
        r1.update()
        self.assertEqual(r1.id, original_id)
        self.assertEqual(r1.width, original_width)
        self.assertEqual(r1.height, original_height)
        self.assertEqual(r1.x, original_x)
        self.assertEqual(r1.y, original_y)

    def test_update_with_kwargs(self):
        """Test updating attributes using kwargs."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)

        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)

    def test_update_with_args(self):
        """Test updating attributes using args."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_update_with_args_and_kwargs(self):
        """Test that kwargs do not overwrite args."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, height=3)  # height should remain 10
        self.assertEqual(r1.height, 10)  # Check that height is still 10


if __name__ == "__main__":
    unittest.main()