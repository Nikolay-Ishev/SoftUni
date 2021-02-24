employee_happiness = input().split()
h_factor = int(input())
employee_happiness = list(map(lambda x: int(x) * h_factor, employee_happiness))
h_score = sum(employee_happiness) / len(employee_happiness)
filtered_list = list(filter(lambda x: x >= h_score, employee_happiness))
if len(filtered_list) >= len(employee_happiness) / 2:
    print(f"Score: {len(filtered_list)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_list)}/{len(employee_happiness)}. Employees are not happy!")
