# n1_input = int(input())
# n2_input = int(input())
# n3_input = int(input())
#
#
# def sum_numbers(n1, n2):
#     return n1 + n2
#
#
# def subtract(n3, n4):
#     return n3 - n4
#
#
# def add_and_subtract():
#     return subtract(sum_numbers(n1_input, n2_input), n3_input)
#
#
# print(add_and_subtract())


# ----------------------2 вариант----------------------------------------

def add_and_subtract(first_n, second_n, third_n):
    def sum_numbers(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    return subtract(sum_numbers(first_n, second_n), third_n)


a = int(input())
b = int(input())
c = int(input())
print(add_and_subtract(a, b, c))
