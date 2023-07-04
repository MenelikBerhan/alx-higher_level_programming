#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for `max_integer` function"""

    def test_normal_list(self):
        """Test for a list with unique max value"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_normal_list2(self):
        """Test for a list with multiple max value"""
        self.assertEqual(max_integer([4, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 13, 13, 2]), 13)

    def test_empty_list(self):
        """Test for empty list argument"""
        self.assertIsNone(max_integer([]))

    def test_list_one(self):
        """Test for a list with one element as an argument"""
        self.assertEqual(max_integer([-1]), -1)

    def test_edge_case(self):
        """Test for a list with all elements of the same type other
        than `int` or `float`"""
        self.assertEqual(max_integer(['1', '2', '3', '4']), '4')
        self.assertEqual(max_integer([['1'], ['3'], ['4'], ['2']]), ['4'])

    def test_edge_case2(self):
        """Test for a list with elements of different type other
        than `int` or `float`"""
        self.assertRaises(TypeError, max_integer, [1, ['2'], {'a': 0}, '4'])
        self.assertRaises(TypeError, max_integer, ['1', ['3'], 4, ('2',)])

    def test_edge_case3(self):
        """Test for a list with multiple max values in `int` and `float`"""
        self.assertEqual(max_integer([4, 2, 3, 4.0]), 4)
        self.assertEqual(max_integer([1, 13.0, 13, 2]), 13.0)

    def test_edge_case3(self):
        """Test for a call without any argument"""
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
