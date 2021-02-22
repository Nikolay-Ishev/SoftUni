number = float(input())
coins = 0
while number > 0:
    if number - 2 >= 0:
        number -= 2
    elif number - 1 >= 0:
        number -= 1
    elif number - 0.5 >= 0:
        number -= 0.5
    elif number - 0.2 >= 0:
        number -= 0.2
    elif number - 0.1 >= 0:
        number -= 0.1
    elif number - 0.05 >= 0:
        number -= 0.05
    elif number - 0.02 >= 0:
        number -= 0.02
    elif number - 0.01 >= 0:
        number -= 0.01
    coins += 1
    number = round(number, 2)
print(coins)

