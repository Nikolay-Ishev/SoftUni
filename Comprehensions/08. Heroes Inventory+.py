heroes = input().split(", ")
command = input()
inventory = {x: {} for x in heroes}
while command != "End":
    name, item, cost = command.split("-")
    if item not in inventory[name]:
        inventory[name][item] = int(cost)
    command = input()
for key, value in inventory.items():
    print(f"{key} -> Items: {len(value)}, Cost: {sum(value[x] for x in value)}")
