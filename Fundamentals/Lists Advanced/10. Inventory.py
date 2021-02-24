def collect(item, inventory):
    if item not in inventory:
        inventory.append(item)


def drop(item, inventory):
    if item in inventory:
        inventory.remove(item)


def combine(item, inventory):
    items = item.split(":")
    if items[0] in inventory:
        inventory.insert((inventory.index(items[0]) + 1), items[1])


def renew(item, inventory):
    if item in inventory:
        inventory.append(inventory.pop(inventory.index(item)))


item_list = input().split(", ")
command = input().split(" - ")
while command[0] != "Craft!":
    if command[0] == "Collect":
        collect(command[1], item_list)
    elif command[0] == "Drop":
        drop(command[1], item_list)
    elif command[0] == "Combine Items":
        combine(command[1], item_list)
    elif command[0] == "Renew":
        renew(command[1], item_list)
    command = input().split(" - ")
print(', '.join([str(elem) for elem in item_list]))


