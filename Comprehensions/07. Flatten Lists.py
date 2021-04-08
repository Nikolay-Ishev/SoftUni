str_list = [[int(n) for n in x.split()] for x in input().split("|")]
print(*[num for sublist in str_list[::-1] for num in sublist])


