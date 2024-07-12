import unittest
from simple_calculator import SimpleCalculator

class TestCase(unittest.TestCase):
    def test_addition(self):
        result = SimpleCalculator.add(0,10,5)
        self.assertEqual(result,15)

    def test_subraction(self):
        result = SimpleCalculator.subtract(0,10,5)
        self.assertEqual(result,5)

    def test_multiplication(self):
        result = SimpleCalculator.multiply(0,10,5)
        self.assertEqual(result,50)

    def test_divesion(self):
        result = SimpleCalculator.divide(0,10,5)
        self.assertEqual(result,2)

    def test_divesion_by_0(self):
       try:
        result = SimpleCalculator.divide(0,10,0)
        self.assertEqual(result,None)
       except ZeroDivisionError as e:
           print(e)

       finally:
           print("you cannot divide by zero")