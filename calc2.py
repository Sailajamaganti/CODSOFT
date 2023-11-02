import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Invalid input. Square root of a negative number is undefined."
    return math.sqrt(x)

while True:
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter '**' for exponentiation")
    print("Enter 'sqrt' for square root")
    print("Enter 'end' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("+", "-", "*", "/", "**", "sqrt"):
        if user_input == "sqrt":
            num = float(input("Enter a number: "))
            result = square_root(num)
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if user_input == "+":
                result = add(num1, num2)
            elif user_input == "-":
                result = subtract(num1, num2)
            elif user_input == "*":
                result = multiply(num1, num2)
            elif user_input == "/":
                result = divide(num1, num2)
            elif user_input == "**":
                result = power(num1, num2)
        print("Result: " + str(result))
    else:
        print("Invalid input. Please enter a valid operation.")
