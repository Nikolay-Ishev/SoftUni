rows, columns = (int(x) for x in input().split())
matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split()])
command = input()
while command != "END":
    command = command.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        command = input()
        continue
    row_1, column_1, row_2, column_2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
    if row_1 not in range(rows) or column_1 not in range(columns) \
            or row_2 not in range(rows) or column_2 not in range(columns):
        print("Invalid input!")
        command = input()
        continue
    matrix[row_1][column_1], matrix[row_2][column_2] \
        = matrix[row_2][column_2], matrix[row_1][column_1]
    for e in matrix:
        print(*e)
    command = input()

