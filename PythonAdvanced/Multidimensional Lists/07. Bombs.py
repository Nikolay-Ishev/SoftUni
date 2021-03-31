def explode(explosive, r, c, board):
    if r - 1 >= 0:
        if board[r - 1][c] > 0:
            board[r-1][c] -= explosive
        if c - 1 >= 0:
            if board[r-1][c-1] > 0:
                board[r-1][c-1] -= explosive
        if c + 1 < len(board):
            if board[r-1][c+1] > 0:
                board[r-1][c+1] -= explosive
    if r + 1 < len(board):
        if board[r+1][c] > 0:
            board[r+1][c] -= explosive
        if c - 1 >= 0:
            if board[r + 1][c - 1] > 0:
                board[r + 1][c - 1] -= explosive
        if c + 1 < len(board):
            if board[r + 1][c + 1] > 0:
                board[r + 1][c + 1] -= explosive
    if c - 1 >= 0:
        if board[r][c-1] > 0:
            board[r][c-1] -= explosive
    if c + 1 < len(board):
        if board[r][c+1] > 0:
            board[r][c+1] -= explosive
    if board[r][c] > 0:
        board[r][c] = 0
    return board


matrix_size = int(input())
matrix = []
for row in range(matrix_size):
    matrix.append([int(x) for x in input().split()])
bombs = input().split()
# bomb_value = []
# # for bomb_i in range(len(bombs)):
# #     row, col = [int(x) for x in bombs[bomb_i].split(",")]
# #     bomb_value.append(matrix[row][col])
for bomb_i in range(len(bombs)):
    row, col = [int(x) for x in bombs[bomb_i].split(",")]
    # bomb = bomb_value[bomb_i]
    bomb = matrix[row][col]
    if bomb > 0:
        matrix = explode(bomb, row, col, matrix)

alive_cells = 0
alive_cells_sum = 0
for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] > 0:
            alive_cells += 1
            alive_cells_sum += matrix[row][col]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")
for row in matrix:
    print(*row)

