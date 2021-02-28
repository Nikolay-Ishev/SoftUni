energy = int(input())
power = True
wins = 0
command = input()
while command != "End of battle":
    distance = int(command)
    if distance <= energy:
        wins += 1
        energy -= distance
        if wins % 3 == 0:
            energy += wins
    else:
        power = False
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break
    command = input()
if power:
    print(f"Won battles: {wins}. Energy left: {energy}")





