n = int(input())
current = 1
for rows in range(1, n + 1):
    for row_numbers in range(1, rows + 1):
        if current > n:
            break
        print(current, end=" ")
        current += 1
    if current > n:
        break
    print()



