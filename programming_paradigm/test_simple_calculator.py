import unittest
from simple_calculator import SimpleCalculator

class TestCase(unittest.TestCase):
    def __int__(self):
        self.calc=SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(10,5),15)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,5),5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,10),50)

    def test_division(self):
        self.assertEqual(self.calc.divide(10,5),2)
        self.assertEqual(self.calc.divide(10,0),None)