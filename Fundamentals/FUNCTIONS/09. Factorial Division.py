import math


def factorial_division(a, b):
    return f"{(math.factorial(a) / math.factorial(b)):.2f}"


input_a = int(input())
input_b = int(input())
print(factorial_division(input_a, input_b))



