def calculator():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b != 0:
            result = a / b
        else:
            return "Division by zero is not allowed"
    else:
        return "Invalid operation selected"

    return f"{a} {operation} {b} = {result}"
