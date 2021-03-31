# for i in range(5,-1,-1):
#     print(i)-012345
matrix = []
for row in range(int(input())):
    matrix.append([int(x) for x in input().split()])
prim_diagonal = []
second_diagonal = []
for row in range(len(matrix) - 1, -1, -1):
    prim_diagonal.append(matrix[row][row])
    second_diagonal.append(matrix[row][len(matrix) - 1 - row])
print(abs(sum(prim_diagonal) - sum(second_diagonal)))




