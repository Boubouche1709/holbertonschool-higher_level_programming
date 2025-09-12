#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when max value is the first element"""
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_one_element(self):
        """Test with a single-element list"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-10, -3, -5, -1]), -1)

    def test_mixed_numbers(self):
        """Test with positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 3, -2]), 5)

    def test_identical_numbers(self):
        """Test with identical numbers"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)


if __name__ == '__main__':
    unittest.main()
