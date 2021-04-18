from functools import reduce


def multiply_with_reduce(*args):
    return reduce(lambda x, y: x * y, args)


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
