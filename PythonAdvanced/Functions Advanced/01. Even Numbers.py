def even_numbers(x):
    if x % 2 == 0:
        return True
    else:
        return False


even_n = filter(even_numbers, [int(x) for x in input().split()])
even_list = []
for n in even_n:
    even_list.append(n)
print(even_list)

