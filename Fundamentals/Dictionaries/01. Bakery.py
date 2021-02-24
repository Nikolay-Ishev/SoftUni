item_list = input().split()
bakery = {}
for index in range(0, len(item_list), 2):
    key = item_list[index]
    value = int(item_list[index + 1])
    bakery[key] = value
print(bakery)
