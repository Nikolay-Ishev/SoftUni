def valid_coord_check(a, b, n):
    # row, col, board_size
    if 0 <= a < n and 0 <= b < n:
        return True
    return False


matrix_size = int(input())
matrix = [[0 for c in range(matrix_size)] for r in range(matrix_size)]
for bomb in range(int(input())):
    row, col = input().split(", ")
    row = int(row[1:])
    col = int(col[:-1])
    matrix[row][col] = "*"

moves = ((-1, 0), (+1, 0), (0, -1), (0, +1), (-1, -1), (-1, +1), (+1, -1), (+1, +1))

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == "*":
            continue
        else:
            mines = 0
            for i in range(len(moves)):
                current_row = moves[i][0]
                current_col = moves[i][1]
                if not valid_coord_check(row + current_row, col + current_col, matrix_size):
                    continue
                if matrix[row + current_row][col + current_col] == "*":
                    mines += 1
            matrix[row][col] = mines
for el in matrix:
    print(*el)
