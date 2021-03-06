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
    
    def is_multiple_of_5_but_not_3(self):
        x = 5
        actual = fizzChecker.isCorrect(x)
        self.assertTrue(actual)

    def is_multiple_of_5_and_3(self):
        x = 15
        actual = fizzChecker.isCorrect(x)
        self.assertTrue(actual)

    def repeat_self_if_not_multiple_of_3_or_5_and_is_positive(self):
        x = 2
        actual = fizzChecker.isCorrect(x)
        self.assertFalse(actual)

