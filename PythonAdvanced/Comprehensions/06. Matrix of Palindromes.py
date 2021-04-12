def palindrome(row, column):
    a = chr(ord('a') + row)
    b = chr(ord('a') + row + column)
    return a + b + a


r, c = (int(x) for x in input().split())
matrix = [[palindrome(row, column) for column in range(c)] for row in range(r)]
[print(*matrix[row]) for row in range(r)]

