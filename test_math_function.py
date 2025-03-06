import unittest
from math_function import increment, multiply_by_two, is_even
# Test Class
class TestMathFunctions(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(increment(3), 4)
        self.assertEqual(increment(5), 6)
        self.assertEqual(increment(-2), -1)
    # Test for validation
    def test_multiply_by_two(self):
        self.assertEqual(multiply_by_two(3), 6)
        self.assertEqual(multiply_by_two(0), 0)
        self.assertEqual(multiply_by_two(-4), -8)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))
        self.assertTrue(is_even(0))