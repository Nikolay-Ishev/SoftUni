def shoot(i, p, old_list):
    i = int(i)
    p = int(p)
    if 0 <= i < len(old_list):
        old_list[i] -= p
        if old_list[i] <= 0:
            old_list.pop(i)
    return old_list


def add(i, v, old_list):
    i = int(i)
    v = int(v)
    if 0 <= i < len(old_list):
        old_list.insert(i, v)
    else:
        print("Invalid placement!")
    return old_list


def strike(i, r, old_list):
    i = int(i)
    r = int(r)
    if 0 <= i < len(old_list):
        if i - r >= 0 and i + r < len(old_list):
            new_list = old_list[0:(i - r)] + old_list[(i + r + 1):]
            return new_list
    print("Strike missed!")
    return old_list


targets = input().split()
targets = [int(x) for x in targets]
command = input()
while command != "End":
    command = command.split()
    if command[0] == "Shoot":
        targets = shoot(command[1], command[2], targets)
    elif command[0] == "Add":
        targets = add(command[1], command[2], targets)
    elif command[0] == "Strike":
        targets = strike(command[1], command[2], targets)
    command = input()
targets = [str(n) for n in targets]
print("|".join(targets))
