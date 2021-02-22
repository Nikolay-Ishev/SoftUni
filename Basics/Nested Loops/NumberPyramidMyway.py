n = int(input())
current = 1
row = 1
while current <= n:
    for numbers in range(row):
        if current > n:
            break
        print(current, end=" ")
        current += 1
    if current > n:
        break
    print()
    row += 1
