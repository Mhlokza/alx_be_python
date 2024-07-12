import unittest
from simple_calculator import SimpleCalculator

class TestCase(unittest.TestCase):
    def test_addition(self):
        result = SimpleCalculator().add(10,5)
        self.assertEqual(self,result,15)

    def test_subraction(self):
        result = SimpleCalculator().subtract(10,5)
        self.assertEqual(self,result,5)

    def test_multiplication(self):
        result = SimpleCalculator().multiply(10,5)
        self.assertEqual(self,result,50)

    def test_divesion(self):
        result = SimpleCalculator().divide(10,5)
        self.assertEqual(self,result,2)

    def test_divesion_by_0(self):
       try:
        result = SimpleCalculator().divide(10,0)
        self.assertEqual(self,result,None)
       except ZeroDivisionError as e:
           print(e)

       finally:
           print("you cannot divide by zero")