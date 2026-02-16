# Exercise 1: Simple Calculator Module
import calculator

try:
    x = float(input("Enter 1st number: "))
    y = float(input("Enter 2nd number: "))
    operation = input("Select any airthmatic option (+, -, *, /): ")

    if operation == "+":
        print("Result:", calculator.add(x, y))
    elif operation == "-":
        print("Result:", calculator.subtract(x, y))
    elif operation == "*":
        print("Result:", calculator.multiply(x, y))
    elif operation == "/":
        print("Result:", calculator.divide(x, y))
    else:
        print("Invalid operation")

except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Invalid input")


# Exercise 2: Math Quiz with Exception Handling
import random

a = random.randint(1, 10)
b = random.randint(1, 10)

print("\nMath Quiz:")
print(a, "+", b)

try:
    answer = int(input("Your answer: "))
    if answer == a + b:
        print("Correct!")
    else:
        print("Wrong answer.")
except ValueError:
    print("Invalid input!")


# Exercise 3: Scoped Variables Experiment
x = "Outside variable"

def scope_test():
    x = "Inside function"
    print("Inside function:", x)

scope_test()
print("Outside function:", x)
