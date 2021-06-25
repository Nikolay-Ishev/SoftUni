from collections import deque
pizzas = deque(int(x) for x in input().split(", "))
employees = [int(x) for x in input().split(", ")]
total_pizzas_made = 0
while pizzas and employees:
    if 0 >= pizzas[0] or pizzas[0] > 10:
        pizzas.popleft()
    elif pizzas[0] > employees[-1]:
        pizzas[0] -= employees[-1]
        total_pizzas_made += employees[-1]
        employees.pop()
    else:
        total_pizzas_made += pizzas[0]
        pizzas.popleft()
        employees.pop()
if not pizzas:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizzas)}")

