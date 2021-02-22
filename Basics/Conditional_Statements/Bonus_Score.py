number = int(input())
if number <= 100:
    bonus = 5
elif 100 < number <= 1000:
    bonus = 0.2 * number
else:
    bonus = 0.1 * number
if number % 2 == 0:
    full_bonus = bonus + 1
elif number % 10 == 5:
    full_bonus = bonus + 2
else:
    full_bonus = bonus
print(full_bonus)
print(full_bonus + number)

# Може да се създаде променлива "bonus = 0" в началото и да добавям стойности с "bonus += (стойност)"







