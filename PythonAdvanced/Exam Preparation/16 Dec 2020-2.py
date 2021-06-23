def valid_coord_check(a, b, n):
    # row, col, board_size
    if 0 <= a < n and 0 <= b < n:
        return True
    return False


moves_dict = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}


def run_command_simplified(command, matrix, p_position, current_message):
    p_row = p_position[0]
    p_col = p_position[1]
    row_move = p_row + moves_dict[command][0]
    col_move = p_col + moves_dict[command][1]
    if not valid_coord_check(row_move, col_move, len(matrix)):
        current_message.pop()
        return matrix, p_position, current_message
    else:
        matrix[p_row][p_col] = "-"
        if matrix[row_move][col_move] != "-":
            current_message.append(matrix[row_move][col_move])
        matrix[row_move][col_move] = "P"
        p_position = row_move, col_move
        return matrix, p_position, current_message


# def run_command(command, matrix, p_position, current_message):
#     p_row = p_position[0]
#     p_col = p_position[1]
#     if command == "up":
#         if not valid_coord_check(p_row - 1, p_col, len(matrix)):
#             current_message.pop()
#             return matrix, p_position, current_message
#         else:
#             matrix[p_row][p_col] = "-"
#             if matrix[p_row - 1][p_col] != "-":
#                 current_message.append(matrix[p_row - 1][p_col])
#             matrix[p_row - 1][p_col] = "P"
#             p_position = p_row - 1, p_col
#             return matrix, p_position, current_message
#     elif command == "down":
#         if not valid_coord_check(p_row + 1, p_col, len(matrix)):
#             current_message.pop()
#             return matrix, p_position, current_message
#         else:
#             matrix[p_row][p_col] = "-"
#             if matrix[p_row + 1][p_col] != "-":
#                 current_message.append(matrix[p_row + 1][p_col])
#             matrix[p_row + 1][p_col] = "P"
#             p_position = p_row + 1, p_col
#             return matrix, p_position, current_message
#     elif command == "left":
#         if not valid_coord_check(p_row, p_col - 1, len(matrix)):
#             current_message.pop()
#             return matrix, p_position, current_message
#         else:
#             matrix[p_row][p_col] = "-"
#             if matrix[p_row][p_col - 1] != "-":
#                 current_message.append(matrix[p_row][p_col - 1])
#             matrix[p_row][p_col - 1] = "P"
#             p_position = p_row, p_col - 1
#             return matrix, p_position, current_message
#     elif command == "right":
#         if not valid_coord_check(p_row, p_col + 1, len(matrix)):
#             current_message.pop()
#             return matrix, p_position, current_message
#         else:
#             matrix[p_row][p_col] = "-"
#             if matrix[p_row][p_col + 1] != "-":
#                 current_message.append(matrix[p_row][p_col + 1])
#             matrix[p_row][p_col + 1] = "P"
#             p_position = p_row, p_col + 1
#             return matrix, p_position, current_message


def find_player(matrix):
    for row_i in range(len(matrix)):
        for col_i in range(len(matrix[row_i])):
            if matrix[row_i][col_i] == "P":
                return row_i, col_i


current_message = [x for x in input()]
m_size = int(input())
matrix = []

for r in range(m_size):
    matrix.append([])
    for el in input():
        matrix[r].append(el)

p_cords = find_player(matrix)
for _ in range(int(input())):
    command = input()
    matrix, p_cords, current_message = run_command_simplified(command, matrix, p_cords, current_message)
print(*current_message, sep="")
for row in range(len(matrix)):
    print(*matrix[row], sep="")
