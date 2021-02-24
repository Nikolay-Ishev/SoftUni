quantity = int(input())
days_left = int(input())
counter = 0
money = 0
spirit = 0
for day in range(days_left, 0, -1):
    counter += 1
    if counter % 11 == 0:
        quantity += 2
    if counter % 2 == 0:
        money += quantity * 2
        spirit += 5
    if counter % 3 == 0:
        money += quantity * 5 + quantity * 3
        spirit += 13
    if counter % 5 == 0:
        money += quantity * 15
        spirit += 17
        if counter % 3 == 0:
            spirit += 30
    if counter % 10 == 0:
        spirit -= 20
        money += 23

if counter % 10 == 0:
    spirit -= 30
print(f"Total cost: {money}")
print(f"Total spirit: {spirit}")


