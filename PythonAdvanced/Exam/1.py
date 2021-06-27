from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milks = deque([int(x) for x in input().split(", ")])
milkshakes = 0
while chocolates and milks:
    if milkshakes == 5:
        break
    current_chocolate = chocolates[-1]
    current_milk = milks[0]
    if current_chocolate <= 0:
        chocolates.pop()
        if current_milk <= 0:
            milks.popleft()
        continue
    elif current_milk <= 0:
        milks.popleft()
        continue
    if current_chocolate == current_milk:
        milkshakes += 1
        chocolates.pop()
        milks.popleft()
    else:
        milks.append(milks.popleft())
        chocolates[-1] -= 5
        if chocolates[-1] <= 0:
            chocolates.pop()
if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")
if milks:
    print(f"Milk: {', '.join(str(x) for x in milks)}")
else:
    print("Milk: empty")
