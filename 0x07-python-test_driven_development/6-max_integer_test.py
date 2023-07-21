""" In this module the test cases for the funciton max_integer
is evaluated."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test cases for max_integer() function. """

    def test_max(self):
        """ Tests max_integer with functional cases. """
        self.assertEqual(max_integer([0, 1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([0, 1]), 1)
        self.assertEqual(max_integer([-1, 2]), 2)
        self.assertEqual(max_integer([0, 10, 2]), 10)
        self.assertEqual(max_integer([-100]), -100)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_integer("Hello29z"), 'z')
        self.assertEqual(max_integer({1: 100, 2: 300, 3: 0, 0: 500}), 500)

    def test_values(self):
        """ Test error cases. """
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer(["hello", "Python", 3, {'World': 'yes'}])
        with self.assertRaises(KeyError):
            max_integer({22: "hello", "today": 25})
