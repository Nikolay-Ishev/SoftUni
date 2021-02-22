food_kg = int(input())
command = input()
grams_total = 0
while command != "Adopted":
    grams_per_day = int(command)
    grams_total += grams_per_day
    command = input()
if food_kg * 1000 >= grams_total:
    print(f"Food is enough! Leftovers: {(food_kg * 1000) - grams_total} grams.")
else:
    print(f"Food is not enough. You need {grams_total - (food_kg * 1000)} grams more.")
