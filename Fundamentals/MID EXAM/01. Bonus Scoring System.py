students = int(input())
lectures = int(input())
bonus = int(input())
attendances = []
for n in range(students):
    x = int(input())
    attendances.append(x)
if students == 0:
    n = 0
    total_bonus = 0
else:
    n = max(attendances)
    total_bonus = n / lectures * (5 + bonus)
print(f"Max Bonus: {round(total_bonus)}.")
print(f"The student has attended {round(n)} lectures.")
