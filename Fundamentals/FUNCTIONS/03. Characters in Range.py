def ch_in_range(a, b):
    string_1 = ""
    for char in range(ord(a) + 1, ord(b)):
        string_1 += str(f"{chr(char)} ")
    return string_1


input_a = input()
input_b = input()
print(ch_in_range(input_a, input_b))


