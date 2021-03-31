def knight_in_range_check(a, b, m):
    knights_in_range = 0
    if a - 2 >= 0:
        if b - 1 >= 0:
            if m[a - 2][b - 1] != "0":
                knights_in_range += 1
        if b + 1 < len(m):
            if m[a - 2][b + 1] != "0":
                knights_in_range += 1
    if a + 2 < len(m):
        if b - 1 >= 0:
            if m[a + 2][b - 1] != "0":
                knights_in_range += 1
        if b + 1 < len(m):
            if m[a + 2][b + 1] != "0":
                knights_in_range += 1
    if b - 2 >= 0:
        if a - 1 >= 0:
            if m[a - 1][b - 2] != "0":
                knights_in_range += 1
        if a + 1 < len(m):
            if m[a + 1][b - 2] != "0":
                knights_in_range += 1
    if b + 2 < len(m):
        if a - 1 >= 0:
            if m[a - 1][b + 2] != "0":
                knights_in_range += 1
        if a + 1 < len(m):
            if m[a + 1][b + 2] != "0":
                knights_in_range += 1
    return knights_in_range

# def valid_coord_check(a, b, n):
#     if 0 <= a < n and 0 <= b < n:
#         return True
#     return False
#
#
# def knight_in_range_check(a, b, m):
#     knights_in_range = 0
#     rows = [-2, -2, 2, 2, 1, 1, -1, -1]
#     cols = [-1, 1, -1, 1, -2, 2, -2, 2]
#     for i in range(len(rows)):
#         current_row = a + rows[i]
#         current_col = b + cols[i]
#         if valid_coord_check(current_row, current_col, board_size):
#             position = matrix[current_row][current_col]
#             if position == "K":
#                 knights_in_range += 1
#     return knights_in_range


board_size = int(input())
matrix = []
removed_knights = 0

for row in range(board_size):
    matrix.append([x for x in input()])

max_knights_in_range = 0
current_knights_in_range = 0
best_knight_index = []
knight_in_range = True
while knight_in_range:
    for row_i in range(board_size):
        for col_i in range(board_size):
            if matrix[row_i][col_i] == "0":
                continue
            current_knights_in_range += knight_in_range_check(row_i, col_i, matrix)
            if current_knights_in_range > max_knights_in_range and current_knights_in_range > 0:
                max_knights_in_range = current_knights_in_range
                best_knight_index.clear()
                best_knight_index.append(row_i)
                best_knight_index.append(col_i)
            current_knights_in_range = 0
    if best_knight_index:
        matrix[best_knight_index[0]][best_knight_index[1]] = "0"
        removed_knights += 1
        best_knight_index.clear()
        max_knights_in_range = 0
    else:
        knight_in_range = False
print(removed_knights)
