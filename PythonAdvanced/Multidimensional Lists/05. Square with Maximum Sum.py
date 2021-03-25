import sys

rows, columns = (int(x) for x in input().split(", "))
matrix = []
submatrix_sum = - sys.maxsize
submatrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
for row in range(rows - 1):
    for column in range(columns - 1):
        current_submatrix = [[matrix[row][column], matrix[row][column + 1]],
                             [matrix[row + 1][column], matrix[row + 1][column + 1]]]
        if sum(current_submatrix[0]) + sum(current_submatrix[1]) > submatrix_sum:
            submatrix_sum = sum(current_submatrix[0]) + sum(current_submatrix[1])
            submatrix = current_submatrix
for m in submatrix:
    print(*m)
print(submatrix_sum)

