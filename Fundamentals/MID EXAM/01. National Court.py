employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
people = int(input())
hour = 0
while people > 0:
    hour += 1
    if hour % 4 == 0:
        continue
    people -= employee_1 + employee_2 + employee_3
print(f"Time needed: {hour}h.")

