def get_magic_triangle(n):
    n = int(n)
    triangle = [[1], [1, 1]]
    while len(triangle) < n:
        new_row = []
        for i in range(len(triangle[-1]) + 1):
            if i == 0 or i == len(triangle[-1]):
                new_row.append(1)
            else:
                number = triangle[-1][i] + triangle[-1][i - 1]
                new_row.append(number)
        triangle.append(new_row.copy())
        new_row.clear()
    return triangle


get_magic_triangle(5)

