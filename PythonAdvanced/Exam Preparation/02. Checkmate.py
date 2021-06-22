def valid_coord_check(a, b, n):
    # row, col, board_size
    if 0 <= a < n and 0 <= b < n:
        return True
    return False


def vertical_up_moves(board, position):
    row_i, col_i = position[0], position[1]
    for row in range(row_i, -1, -1):
        if board[row][col_i] == "Q":
            return [row, col_i]


def vertical_down_moves(board, position):
    row_i, col_i = position[0], position[1]
    for row in range(row_i, len(board)):
        if board[row][col_i] == "Q":
            return [row, col_i]


def horizontal_right_moves(board, position):
    row_i, col_i = position[0], position[1]
    for col in range(col_i, len(board)):
        if board[row_i][col] == "Q":
            return [row_i, col]


def horizontal_left_moves(board, position):
    row_i, col_i = position[0], position[1]
    for col in range(col_i, -1, -1):
        if board[row_i][col] == "Q":
            return [row_i, col]


def right_down_diagonal_moves(board, position):
    row_i, col_i = position[0], position[1]
    for row in range(row_i, len(board)):
        if valid_coord_check(row, col_i, len(board)):
            if board[row][col_i] == "Q":
                return [row, col_i]
            col_i += 1
        else:
            return


def left_up_diagonal_moves(board, position):
    row_i, col_i = position[0], position[1]
    for row in range(row_i, -1, -1):
        if valid_coord_check(row, col_i, len(board)):
            if board[row][col_i] == "Q":
                return [row, col_i]
            col_i -= 1
        else:
            return


def right_up_diagonal_moves(board, position):
    row_i, col_i = position[0], position[1]
    for row in range(row_i, -1, -1):
        if valid_coord_check(row, col_i, len(board)):
            if board[row][col_i] == "Q":
                return [row, col_i]
            col_i += 1
        else:
            return


def left_down_diagonal_moves(board, position):
    row_i, col_i = position[0], position[1]
    for row in range(row_i, len(board)):
        if valid_coord_check(row, col_i, len(board)):
            if board[row][col_i] == "Q":
                return [row, col_i]
            col_i -= 1
        else:
            return


def check_move(move, queens_list):
    if move:
        queens_list.append(move)


queens = []
chess_board = [[x for x in input().split()] for _ in range(8)]
for row_i in range(len(chess_board)):
    for col_i in range(len(chess_board[row_i])):
        if chess_board[row_i][col_i] == "K":
            kings_position = (row_i, col_i)

check_move(vertical_up_moves(chess_board, kings_position), queens)
check_move(vertical_down_moves(chess_board, kings_position), queens)
check_move(horizontal_right_moves(chess_board, kings_position), queens)
check_move(horizontal_left_moves(chess_board, kings_position), queens)
check_move(right_up_diagonal_moves(chess_board, kings_position), queens)
check_move(right_down_diagonal_moves(chess_board, kings_position), queens)
check_move(left_up_diagonal_moves(chess_board, kings_position), queens)
check_move(left_down_diagonal_moves(chess_board, kings_position), queens)

if not queens:
    print("The king is safe!")
else:
    [print(x) for x in queens]
