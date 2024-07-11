def safe_divide(numerator, denominator):
    if denominator == 0:
        try:
            numerator/denominator
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        else:
            return f"The result of the division is {numerator/denominator}"

num = input("enter the value: ")
try:
    number = float(num)
except ValueError as e:
    print("Error: Please enter numeric values only.")
