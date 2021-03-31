import sys
rows, columns = (int(x) for x in input().split())
matrix = []
submatrix_sum = - sys.maxsize
submatrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split()])
for row in range(rows - 2):
    for column in range(columns - 2):
        current_submatrix = [[matrix[row][column], matrix[row][column + 1], matrix[row][column + 2]],
                             [matrix[row + 1][column], matrix[row + 1][column + 1], matrix[row + 1][column + 2]],
                            [matrix[row + 2][column], matrix[row + 2][column + 1], matrix[row + 2][column + 2]]]
        if sum(current_submatrix[0]) + sum(current_submatrix[1]) + sum(current_submatrix[2]) > submatrix_sum:
            submatrix_sum = sum(current_submatrix[0]) + sum(current_submatrix[1]) + sum(current_submatrix[2])
            submatrix = current_submatrix

print(f"Sum = {submatrix_sum}")
for m in submatrix:
    print(*m)
