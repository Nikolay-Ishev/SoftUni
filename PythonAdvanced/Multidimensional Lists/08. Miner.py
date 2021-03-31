def move(r, c, board_size, command):
    if command == "left":
        if c - 1 >= 0:
            c -= 1
    elif command == "right":
        if c + 1 < board_size:
            c += 1
    elif command == "up":
        if r - 1 >= 0:
            r -= 1
    elif command == "down":
        if r + 1 < board_size:
            r += 1
    return r, c


matrix_size = int(input())
moves = input().split()
matrix = []
for row in range(matrix_size):
    matrix.append([x for x in input().split()])

end = False
coals = 0
current_position = []
for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == "c":
            coals += 1
        elif matrix[row][col] == "s":
            current_position.append(row)
            current_position.append(col)
for step in range(len(moves)):
    current_position[0], current_position[1] = move(current_position[0], current_position[1], matrix_size, moves[step])
    row, col = current_position[0], current_position[1]
    if matrix[row][col] == "c":
        coals -= 1
        matrix[row][col] = "*"
        if coals == 0:
            print(f"You collected all coals! ({row}, {col})")
            end = True
            break
    elif matrix[row][col] == "e":
        print(f"Game over! ({row}, {col})")
        end = True
        break
if not end:
    print(f"{coals} coals left. ({current_position[0]}, {current_position[1]})")

