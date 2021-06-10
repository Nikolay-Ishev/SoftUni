def draw_lines(n):
    row = []
    for j in range(1, n + 1):
        row.append(str(j))
    print(" ".join(row))


def draw_triangle(n):
    for i in range(1, n + 1):
        draw_lines(i)
    for i in range(n - 1, 0, -1):
        draw_lines(i)



