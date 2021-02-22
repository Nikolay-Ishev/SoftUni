cats = int(input())
small = 0
medium = 0
large = 0
food_total = 0
for f in range(cats):
    food = float(input())
    food_total += food
    if food < 200:
        small += 1
    elif food < 300:
        medium += 1
    else:
        large += 1

print(f"Group 1: {small} cats.")
print(f"Group 2: {medium} cats.")
print(f"Group 3: {large} cats.")
print(f"Price for food per day: {((food_total / 1000) * 12.45):.2f} lv.")
