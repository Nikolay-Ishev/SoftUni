destination = input()
saved_money = 0
while destination != "End":
    min_budget = float(input())
    while saved_money < min_budget:
        savings = float(input())
        saved_money += savings
    print(f"Going to {destination}!")
    saved_money = 0
    destination = input()
