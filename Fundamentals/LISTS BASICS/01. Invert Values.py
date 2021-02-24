numbers = input()
numbers_list = numbers.split()
numbers_list = [int(i) for i in numbers_list]
numbers_list = [-i for i in numbers_list]
print(numbers_list)

