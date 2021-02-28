health = 100
bitcoins = 0
rooms = input().split("|")
alive = True
room = 0
for r in rooms:
    command, number = r.split()
    number = int(number)
    room += 1
    if command == "potion":
        if health + number <= 100:
            health += number
            print(f"You healed for {number} hp.")
        else:
            print(f"You healed for {100 - health} hp.")
            health = 100
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            alive = False
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room}")
            break
if alive:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")



