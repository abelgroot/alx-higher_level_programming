import io
import unittest
from unittest.mock import patch

from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset nb_objects before each test"""
        Base._Base__nb_objects = 0  # Reset the id counter for each test

    def test_square_initialization(self):
        """Test initialization of Square instances."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_square_setter(self):
        """Test the size setter method."""
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

    def test_square_setter_invalid_type(self):
        """Test size setter with an invalid type."""
        s1 = Square(5)
        with self.assertRaises(TypeError) as cm:
            s1.size = "9"
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_square_setter_invalid_value(self):
        """Test size setter with an invalid value."""
        s1 = Square(5)
        with self.assertRaises(ValueError) as cm:
            s1.size = -1
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_display(self):
        """Test the display method of Square."""
        s1 = Square(2, 1, 1)
        expected_output = "\n ##\n ##\n"  # 2x2 square with x offset 1 and y offset 1
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            s1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_with_no_offset(self):
        """Test the display method with no x and y offsets."""
        s1 = Square(3)
        expected_output = "###\n###\n###\n"  # 3x3 square with no offsets
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            s1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test the string representation of Square."""
        s1 = Square(5, 1, 1, 1)
        self.assertEqual(str(s1), "[Square] (1) 1/1 - 5")

    def test_update_args(self):
        """Test the update method with *args."""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")  # `id` updated

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")  # `id` and `size` updated

        s1.update(1, 2, 3)
        self.assertEqual(
            str(s1), "[Square] (1) 3/0 - 2"
        )  # `id`, `size`, and `x` updated

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")  # All args updated

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")  # Initial

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/0 - 5")  # `x` updated via kwargs

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")  # `size` and `y` updated

        s1.update(id=89, size=7, y=1)
        self.assertEqual(
            str(s1), "[Square] (89) 12/1 - 7"
        )  # `id`, `size`, and `y` updated

    def test_update_args_over_kwargs(self):
        """Test that *args is prioritized over **kwargs."""
        s1 = Square(5)
        s1.update(99, 8, 5, 5, id=42, size=4, x=2, y=3)
        self.assertEqual(
            str(s1), "[Square] (99) 5/5 - 8"
        )  # *args takes priority over **kwargs


if __name__ == "__main__":
    unittest.main()
