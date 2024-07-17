class Calculator:
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a, b):
        return f"The sum is: {a+b}"

    @classmethod

    def multiply(cls, a, b):
        print(f"Calculation type: {Calculator.calculation_type}")
        cls.a =a
        cls.b = b
        return f"The product is: {cls.a * cls.b}"