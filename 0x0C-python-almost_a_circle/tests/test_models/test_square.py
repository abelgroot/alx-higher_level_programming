import io
import unittest
from unittest.mock import patch

from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_square_initialization(self):
        """Test initialization of Square instances."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

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
        expected_output = "\n  ##\n  ##\n"  # 2x2 square with x offset 1 and y offset 1
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


if __name__ == "__main__":
    unittest.main()
