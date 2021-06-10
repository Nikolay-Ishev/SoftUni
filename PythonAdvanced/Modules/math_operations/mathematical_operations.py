def multiply(x, y):
    return f"{x * y:.2f}"


def divide(x, y):
    return f"{x / y:.2f}"


def add(x, y):
    return f"{x + y:.2f}"


def subtract(x, y):
    return f"{x - y:.2f}"


def raise_number(x, y):
    return f"{x ** y:.2f}"


def calculate_expressions(x, n, y):
    x, y = float(x), float(y)
    if n == "/":
        print(divide(x, y))
    elif n == "*":
        print(multiply(x, y))
    elif n == "-":
        print(subtract(x, y))
    elif n == "+":
        print(add(x, y))
    elif n == "^":
        print(raise_number(x, y))


