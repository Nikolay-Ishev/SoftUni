energy = 100
coins = 100
event_list = input().split("|")
success = True
for event in event_list:
    ingredient, number = event.split("-")
    number = int(number)
    if ingredient == "rest":
        if number + energy <= 100:
            energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")
        else:
            print(f"You gained {100 - energy} energy.")
            print(f"Current energy: {100}.")
            energy = 100
    elif ingredient == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins <= number:
            print(f"Closed! Cannot afford {ingredient}.")
            success = False
            break
        else:
            coins -= number
            print(f"You bought {ingredient}.")
if success:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")





