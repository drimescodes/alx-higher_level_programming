#!/usr/bin/env python3
"""Unit test for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A class to test the max_integer function.
    """

    def test_ordered(self):
        """
        Test max_integer with ordered list.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered(self):
        """
        Test max_integer with unordered list.
        """
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_ordered_rev(self):
        """
        Test max_integer with reverse ordered list.
        """
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty(self):
        """
        Test max_integer with empty list.
        """
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """
        Test max_integer with one element list.
        """
        self.assertEqual(max_integer([1]), 1)

    def test_floats(self):
        """
        Test max_integer with floats.
        """
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_ints_floats(self):
        """
        Test max_integer with ints and floats together
        """
        self.assertEqual(max_integer([1.55, 3, 8.9, 5, 3.2, 11.1, 4]), 11.1)

    def test_string(self):
        """
        Test a string
        """
        self.assertEqual(max_integer("Ukeme"), 'm')

    def test_lists_strings(self):
        """
        Test a list of strings
        """
        self.assertEqual(max_integer(["Ukeme", "is", "my", "name"]), "name")

    def test_empty_string(self):
        """
        Test empty string
        """
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
