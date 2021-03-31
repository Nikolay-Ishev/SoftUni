rows, columns = (int(x) for x in input().split())
# ma3ix = [["5" for _ in range(5)] for _ in range(5)]

matrix = []
equal_matrices = 0
for row in range(rows):
    matrix.append(input().split())
for row in range(rows - 1):
    for column in range(columns - 1):
        submatrix = [[matrix[row][column], matrix[row][column + 1]],
                     [matrix[row + 1][column], matrix[row + 1][column + 1]]]
        if (submatrix[0].count(submatrix[0][0])) + (submatrix[1].count(submatrix[0][0])) == 4:
            equal_matrices += 1
print(equal_matrices)
# [print(r) for r in ma3ix]
