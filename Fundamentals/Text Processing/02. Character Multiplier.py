a_list = input().split()
longest_str = max(a_list, key=len)
sum = 0
for i in range(0, len(longest_str)):
    if i > len(a_list[0]) - 1:
        sum += ord(a_list[1][i])
    elif i > len(a_list[1]) - 1:
        sum += ord(a_list[0][i])
    else:
        sum += ord(a_list[0][i]) * ord(a_list[1][i])
print(sum)



