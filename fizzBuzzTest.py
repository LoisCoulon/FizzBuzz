import unittest
from fizzCheck import *

class FizzBuzzTest(unittest.TestCase):

    def test_raise_error_if_0(self):
        with self.assertRaises(ArgumentError):
            x = 0
            actual = fizzChecker.isCorrect(x)
    
    def test_raise_error_if_negative(self):
        with self.assertRaises(ArgumentError):
            x = -1
            actual = fizzChecker.isCorrect(x)

    def is_multiple_of_3_but_not_5(self):
        x = 3
        actual = fizzChecker.isCorrect(x)
        self.assertTrue(actual)
    



