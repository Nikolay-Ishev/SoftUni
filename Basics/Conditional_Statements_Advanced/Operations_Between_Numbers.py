n1 = int(input())
n2 = int(input())
operator = str(input())
if operator == "+":
    if (n1 + n2) % 2 == 0:
        type1 = "even"
    else:
        type1 = "odd"
    print(f"{n1} {operator} {n2} = {n1 + n2} - {type1}")
elif operator == "-":
    if (n1 - n2) % 2 == 0:
        type1 = "even"
    else:
        type1 = "odd"
    print(f"{n1} {operator} {n2} = {n1 - n2} - {type1}")
elif operator == "*":
    if (n1 * n2) % 2 == 0:
        type1 = "even"
    else:
        type1 = "odd"
    print(f"{n1} {operator} {n2} = {n1 * n2} - {type1}")
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} / {n2} = {(n1 / n2):.2f}")
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} % {n2} = {n1 % n2}")
