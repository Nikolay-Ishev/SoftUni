def register(username, license):
    if username in parking:
        print(f"ERROR: already registered with plate number {parking[username]}")
    else:
        parking[username] = license
        print(f"{username} registered {license} successfully")


def unregister(username):
    if username not in parking:
        print(f"ERROR: user {username} not found")
    else:
        del parking[username]
        print(f"{username} unregistered successfully")


parking = {}
number = int(input())
for n in range(number):
    command = input().split()
    if command[0] == "register":
        register(command[1], command[2])
    elif command[0] == 'unregister':
        unregister(command[1])
for key, value in parking.items():
    print(f"{key} => {value}")
