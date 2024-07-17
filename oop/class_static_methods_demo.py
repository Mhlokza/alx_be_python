class Calculator:
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a, b):
        sum = a+b
        return f"The sum is: {sum}"

    @classmethod

    def multiply(cls, a, b):
        print(f"Calculation type: {Calculator.calculation_type}")
        cls.a =a
        cls.b = b
        product = cls.a * cls.b
        return f"The product is: {product}"