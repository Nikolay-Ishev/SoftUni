vacation_cost = float(input())
saved_money = float(input())
spend_times = 0
days = 0
while saved_money < vacation_cost and spend_times < 5:
    action = input()
    money = float(input())
    days += 1
    if action == "spend":
        spend_times += 1
        if money >= saved_money:
            saved_money = 0
        else:
            saved_money -= money
    elif action == "save":
        saved_money += money
        spend_times = 0
if spend_times >= 5:
    print("You can't save the money.")
    print(f"{days}")
else:
    print(f"You saved the money for {days} days.")
