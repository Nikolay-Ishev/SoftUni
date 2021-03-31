def move(r, c, total_r, total_c, command):
    if command == "L":
        if c - 1 >= 0:
            c -= 1
        else:
            return "escape"
    elif command == "R":
        if c + 1 < total_c:
            c += 1
        else:
            return "escape"
    elif command == "U":
        if r - 1 >= 0:
            r -= 1
        else:
            return "escape"
    elif command == "D":
        if r + 1 < total_r:
            r += 1
        else:
            return "escape"
    return r, c


def bunny_multiply(r, c, total_r, total_c, board):
    if c - 1 >= 0:
        if board[r][c - 1] != "B":
            board[r][c - 1] = "N"
    if c + 1 < total_c:
        if board[r][c + 1] != "B":
            board[r][c + 1] = "N"
    if r - 1 >= 0:
        if board[r - 1][c] != "B":
            board[r - 1][c] = "N"
    if r + 1 < total_r:
        if board[r + 1][c] != "B":
            board[r + 1][c] = "N"
    return board


escape = False
rows, cols = (int(x) for x in input().split())
matrix = []
for row in range(rows):
    matrix.append([x for x in input()])
moves = [x for x in input()]
current_position = []
for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "P":
            matrix[row][col] = "."
            current_position.append(row)
            current_position.append(col)
            break
for step in range(len(moves)):
    if move(current_position[0], current_position[1], rows, cols, moves[step]) == "escape":
        escape = True
    else:

        
        current_position[0], current_position[1] = \
            move(current_position[0], current_position[1], rows, cols, moves[step])

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                matrix = bunny_multiply(row, col, rows, cols, matrix)
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "N":
                matrix[row][col] = "B"

    if matrix[current_position[0]][current_position[1]] == "B" or escape:
        break
for row in range(rows):
    print(*matrix[row], sep="")
if escape:
    print(f"won: {current_position[0]} {current_position[1]}")
else:
    print(f"dead: {current_position[0]} {current_position[1]}")
