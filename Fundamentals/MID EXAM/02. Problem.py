def blacklist(n, f):
    if n in f:
        i = f.index(n)
        f[i] = "Blacklisted"
        print(f"{n} was blacklisted.")
    else:
        print(f"{n} was not found.")
    return f


def error(i, f):
    i = int(i)
    if i in range(len(f)) and f[i] != "Blacklisted" and f[i] != "Lost":
        print(f"{f[i]} was lost due to an error.")
        f[i] = "Lost"
        return f
    else:
        return f


def change(i, n, f):
    i = int(i)
    if i in range(len(f)):
        print(f"{f[i]} changed his username to {n}.")
        f[i] = n
    return f


friends = input().split(", ")
command = input()
while command != "Report":
    command = command.split()
    if command[0] == "Blacklist":
        friends = blacklist(command[1], friends)
    elif command[0] == "Error":
        friends = error(command[1], friends)
    elif command[0] == "Change":
        friends = change(command[1], command[2], friends)
    command = input()
bl_n = len([name for name in friends if name == 'Blacklisted'])
lost_n = len([name for name in friends if name == 'Lost'])
print(f"Blacklisted names: {bl_n}")
print(f"Lost names: {lost_n}")
print(*friends, sep=" ")
