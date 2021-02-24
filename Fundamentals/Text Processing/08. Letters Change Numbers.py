strings = input().split()
strings = [a.strip() for a in strings]
total_sum = 0
for e in strings:
    a = e[0]
    b = e[-1]
    number = float(e[1:-1])
    if a.isupper():
        new_number = number / (ord(a) - 64)
    else:
        new_number = number * (ord(a) - 96)

    if b.isupper():
        total_sum += new_number - (ord(b) - 64)
    else:
        total_sum += new_number + (ord(b) - 96)
print(f"{total_sum:.2f}")

