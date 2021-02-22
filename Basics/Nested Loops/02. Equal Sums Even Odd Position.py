first_number = int(input())
second_number = int(input())
for numbers in range(first_number, second_number + 1):
    string_number = str(numbers)
    evens = 0
    odds = 0
    for index, digit in enumerate(string_number):
        if index % 2 == 0:
            evens += int(digit)
        else:
            odds += int(digit)
    if evens == odds:
        print(numbers, end=" ")

