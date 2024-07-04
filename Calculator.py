# Calculator Program

# Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Processing and Output
if operation == '+':
    result = num1 + num2
    print(f"Result: {result}")
elif operation == '-':
    result = num1 - num2
    print(f"Result: {result}")
elif operation == '*':
    result = num1 * num2
    print(f"Result: {result}")
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"Result: {result}")
else:
    print("Error: Invalid operation entered.")
