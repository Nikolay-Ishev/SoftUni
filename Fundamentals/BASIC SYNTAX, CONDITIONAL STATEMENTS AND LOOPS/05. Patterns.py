number = int(input())
for stars in range(1, number + 1):
    print("*" * stars)
for star in range(number - 1, 0, -1):
    print("*" * star)
