n = int(input())
numbers = []
category = []
for num in range(n):
    current_number = int(input())
    numbers.append(current_number)
command = input()
if command == "even":
    for number in numbers:
        if number % 2 == 0:
            category.append(number)
elif command == "odd":
    for number in numbers:
        if number % 2 != 0:
            category.append(number)
elif command == "negative":
    for number in numbers:
        if number < 0:
            category.append(number)
else:
    for number in numbers:
        if number >= 0:
            category.append(number)
print(category)


