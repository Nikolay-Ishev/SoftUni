rows, columns = (int(x) for x in input().split(", "))

matrix = []

for row in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

matrix_sum = 0

for i in range(rows):
    matrix_sum += sum(matrix[i])

print(matrix_sum)
print(matrix)


