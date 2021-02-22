n = int(input())
for number in range(1111, 10000):
    counter = 0
    for digit in str(number):
        if int(digit) == 0:
            continue
        if n % int(digit) == 0:
            counter += 1
    if counter >= 4:
        print(number, end=" ")




