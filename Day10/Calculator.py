from art import logo

print(logo)


# Calculator Functions

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {
    '+': add,
    '-': subtract,
    '/': divide,
    "*": multiply,
}

num1 = float(input("What is the first number?: "))
num2 = float(input("What is the second number?: "))

for key in operations:
    print(key)

operationSym = input("Pick an operation symbol from the operations above: ")
operationKeys = operations.keys()

if operationSym in operationKeys:
    answer = operations[operationSym](num1, num2)
    print(f"{num1} {operationSym} {num2} = {answer}")
else:
    print(f"Operation symbol {operationSym} entered is incorrect.")