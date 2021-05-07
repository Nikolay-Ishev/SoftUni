# command = input()
# numbers = [int(x) for x in input().split()]
#
# if command == "Odd":
#     odd_sum = sum(x for x in numbers if x % 2 != 0) * len(numbers)
#     print(odd_sum)
# else:
#     even_sum = sum(x for x in numbers if x % 2 == 0) * len(numbers)
#     print(even_sum)

command = input()
numbers = [int(x) for x in input().split()]

if command == "Odd":
    odd_sum = sum([x for x in numbers if x % 2 != 0]) * len(numbers)
    print(odd_sum)
else:
    even_sum = sum([x for x in numbers if x % 2 == 0]) * len(numbers)
    print(even_sum)
