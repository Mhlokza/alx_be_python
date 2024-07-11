import unittest
from simple_calculator import SimpleCalculator

class TestCase(unittest.TestCase):
    def test_add(self):
        result = SimpleCalculator().add(10,5)
        self.assertEqual(result,15)

    def test_subr(self):
        result = SimpleCalculator().subtract(10,5)
        self.assertEqual(result,5)

    def test_mult(self):
        result = SimpleCalculator().multiply(10,5)
        self.assertEqual(result,50)

    def test_div(self):
        result = SimpleCalculator().divide(10,5)
        self.assertEqual(result,2)

    def test_div_by_0(self):
       try:
        result = SimpleCalculator().divide(10,0)
        self.assertEqual(result,None)
       except ZeroDivisionError as e:
           print(e)

       finally:
           print("you cannot divide by zero")