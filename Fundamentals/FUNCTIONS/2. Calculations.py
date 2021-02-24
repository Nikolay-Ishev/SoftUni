input_operator = input()
num1 = int(input())
num2 = int(input())


def calculate(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = a / b
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    if result % 2 == 0 or (result + 1) % 2 == 0:
        result = int(result)
    return result


print(calculate(num1, num2, input_operator))

