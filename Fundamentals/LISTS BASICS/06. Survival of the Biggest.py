number_list = [int(x) for x in input().split(" ")]
remove_n = int(input())
for removes in range(remove_n):
    number_list.remove(min(number_list))
print(number_list)
