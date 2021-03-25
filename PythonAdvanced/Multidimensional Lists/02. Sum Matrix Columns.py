rows, columns = (int(x) for x in input().split(", "))

matrix = []

for row in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)
for c_i in range(columns):
    column_sum = 0
    for r_i in range(rows):
        column_sum += matrix[r_i][c_i]
    print(column_sum)

