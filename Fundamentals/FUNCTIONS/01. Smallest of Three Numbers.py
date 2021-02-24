n1_input = int(input())
n2_input = int(input())
n3_input = int(input())


def smallest_n(n1, n2, n3):
    smallest = None
    if n1 < n2 and n1 < n3 or (n1 < n2 and n1 == n3):
        smallest = n1
    elif n2 < n1 and n2 < n3 or (n2 < n3 and n2 == n1):
        smallest = n2
    elif n3 < n1 and n3 < n2 or (n3 < n1 and n3 == n2):
        smallest = n3
    return smallest


print(smallest_n(n1_input, n2_input, n3_input))
