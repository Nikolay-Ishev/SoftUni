n = int(input())
matrix = [[int(x) for x in input().split(", ")] for row in range(n)]
prim_diagonal = []
second_diagonal = []
for row in range(len(matrix) - 1, -1, -1):
    prim_diagonal.append(matrix[row][row])
    second_diagonal.append(matrix[row][len(matrix) - 1 - row])
print(f"First diagonal: {', '.join(str(x) for x in prim_diagonal[::-1])}. Sum: {sum(prim_diagonal)}")
print(f"Second diagonal: {', '.join(str(x) for x in second_diagonal[::-1])}. Sum: {sum(second_diagonal)}")
