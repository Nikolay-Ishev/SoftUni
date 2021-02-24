numbers = input()
numbers_list = numbers.split(", ")
numbers_list = [int(i) for i in numbers_list]
# 1 2 3 4 5 6
beggars = int(input())
# 2
profit_list = [0] * beggars
count_beggars = 0
for profits in range(len(numbers_list)):
    count_beggars += 1
    if count_beggars <= beggars:
        profit_list[count_beggars - 1] += numbers_list[profits]
    else:
        count_beggars = 1
        profit_list[count_beggars - 1] += numbers_list[profits]
        continue
print(profit_list)



