import unittest
from FizzBuzz.fizzCheck import *

class FizzBuzzTest(unittest.TestCase):

    def test_raise_error_if_0(self):
        with self.assertRaises(ArgumentError):
            x = 0
            actual = fizzChecker.isCorrect(x)

