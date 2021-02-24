items = input().split()
odd_items = {}
items = [x.lower() for x in items]
for element in items:
    # if element not in odd_items:
    #     odd_items[element] = 0
    # odd_items[element] += 1
    odd_items[element] = items.count(element)
odd_string = []
for key, value in odd_items.items():
    if value % 2 != 0:
        odd_string.append(key)
print(" ".join(odd_string))


