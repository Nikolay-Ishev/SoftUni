rows, columns = (int(x) for x in input().split())
snake = input()
matrix = []
snake_index = 0
for row in range(rows):
    matrix.append([])
    for column in range(columns):
        if snake_index >= len(snake):
            snake_index = 0
        if row % 2 == 0:
            matrix[row].append(snake[snake_index])
        else:
            matrix[row].insert(0, snake[snake_index])
        snake_index += 1
    print("".join(matrix[row]))
