num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
def perform_operation(num1, num2, operation):
    print("Arithmetic Operations")
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "divide":
        if num2 == 0:
            return "you cannot divide by 0"
        return num1/num2
