command = input()
records = {}
while command != "Log out":
    command = command.split(": ")
    username = command[1]
    if command[0] == "New follower":
        if username not in records:
            records[username] = [0, 0]
    elif command[0] == "Like":
        count = int(command[2])
        if username not in records:
            records[username] = [count, 0]
        else:
            records[username][0] += count
    elif command[0] == "Comment":
        if username not in records:
            records[username] = [0, 1]
        else:
            records[username][1] += 1
    elif command[0] == "Blocked":
        if username not in records:
            print(f"{username} doesn't exist.")
        else:
            records.pop(username)
    command = input()
print(f"{len(records)} followers")
ord_records = dict(sorted(records.items(), key = lambda x: (-sum(x[1]), x[0])))
for key, value in ord_records.items():
    print(f"{key}: {sum(value)}")


