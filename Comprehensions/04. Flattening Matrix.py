n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
print([x for row in matrix for x in row])
# for i in range(n):
#     for x in matrix[i]:
#         print(x)

