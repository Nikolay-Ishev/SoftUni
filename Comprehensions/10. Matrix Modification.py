matrix = []
n = int(input())
for row in range(n):
    matrix.append([int(x) for x in input().split()])
command = input()
while command != "END":
    action, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if len(matrix) > row >= 0 and len(matrix[0]) > col >= 0:
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    command = input()
[print(*n) for n in matrix]
