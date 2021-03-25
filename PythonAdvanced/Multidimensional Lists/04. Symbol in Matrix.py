matrix = []
n = int(input())
for row in range(n):
    matrix.append([x for x in input()])
symbol = input()
found = False
for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            found = True
            print(f"({row}, {col})")
            break
    if found:
        break
if not found:
    print(f"{symbol} does not occur in the matrix")
