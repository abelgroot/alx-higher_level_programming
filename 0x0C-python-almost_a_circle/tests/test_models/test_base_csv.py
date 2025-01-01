#!/usr/bin/python3
""" test_base_csv.py """
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseCSV(unittest.TestCase):

    def setUp(self):
        """Set up instances for testing CSV methods."""
        Base._Base__nb_objects = 0  # Resetting the count for testing
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        self.s1 = Square(5)
        self.s2 = Square(7, 9, 1)

    def test_save_to_file_csv_rectangle(self):
        """Test saving to CSV for Rectangle."""
        Rectangle.save_to_file_csv([self.r1, self.r2])
        with open("Rectangle.csv", mode="r") as file:
            content = file.read()
        expected = "1,10,7,2,8\n2,2,4,0,0\n"
        self.assertEqual(content, expected)

    def test_load_from_file_csv_rectangle(self):
        """Test loading from CSV for Rectangle."""
        Rectangle.save_to_file_csv([self.r1, self.r2])
        loaded_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(loaded_rectangles[0].width, self.r1.width)
        self.assertEqual(loaded_rectangles[1].width, self.r2.width)

    def test_save_to_file_csv_square(self):
        """Test saving to CSV for Square."""
        s1 = Square(5, id=3)  # Explicitly setting ID if needed
        s2 = Square(7, 9, 1, id=6)  # Same here for consistency
        Square.save_to_file_csv([s1, s2])

        with open("Square.csv", "r") as file:
            content = file.read()

        expected = "3,5,0,0\n6,7,9,1\n"
        self.assertEqual(content, expected)

    def test_load_from_file_csv_square(self):
        """Test loading from CSV for Square."""
        Square.save_to_file_csv([self.s1, self.s2])
        loaded_squares = Square.load_from_file_csv()
        self.assertEqual(len(loaded_squares), 2)
        self.assertEqual(loaded_squares[0].size, self.s1.size)
        self.assertEqual(loaded_squares[1].size, self.s2.size)

    def tearDown(self):
        """Remove the CSV files created during tests."""
        import os

        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")


if __name__ == "__main__":
    unittest.main()
