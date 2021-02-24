numbers_list = input().split(", ")
numbers_list = [int(x) for x in numbers_list]
group = 10
while numbers_list:
    result = list(filter(lambda x: x <= group, numbers_list))
    numbers_list = list(filter(lambda x: x > group, numbers_list))
    print(f"Group of {group}'s: {result}")
    group += 10




