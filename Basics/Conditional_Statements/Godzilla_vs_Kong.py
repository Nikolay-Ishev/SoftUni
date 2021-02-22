budget = float(input())
people = int(input())
dress_price = float(input())
decoration = 0.1 * budget
if people > 150:
    final_dress_price = (dress_price - (0.1 * dress_price)) * people
    if budget < (decoration + final_dress_price):
        print("Not enough money!")
        print(f"Wingard needs {((decoration + final_dress_price) - budget):.2f} leva more.")
    else:
        print("Action!")
        print(f"Wingard starts filming with {(budget - decoration - final_dress_price):.2f} leva left.")
else:
    final_dress_price = dress_price * people
    if budget < (decoration + final_dress_price):
        print("Not enough money!")
        print(f"Wingard needs {((decoration + final_dress_price) - budget):.2f} leva more.")
    else:
        print("Action!")
        print(f"Wingard starts filming with {(budget - decoration - final_dress_price):.2f} leva left.")
