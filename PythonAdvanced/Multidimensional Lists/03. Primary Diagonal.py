matrix = []
for row in range(int(input())):
    matrix.append([int(x) for x in input().split()])

main_diagonal = 0
for i in range(len(matrix)):
    main_diagonal += matrix[i][i]
print(main_diagonal)
