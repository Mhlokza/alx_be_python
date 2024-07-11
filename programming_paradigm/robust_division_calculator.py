def safe_divide(numerator, denominator):
    if denominator == 0:
        try:
            numerator/denominator
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        else:
            return f"The result of the division is {numerator/denominator}"

numerator = input("enter the value: ")
denominator= input("enter the value: ")
try:
    number = float(numerator), float(denominator)
except ValueError as e:
    print("Error: Please enter numeric values only.")
