friends = input().split(", ")

command = input()
while command != "Report":
    command = command.split()
    if command[0] == "Blacklist":
        name = command[1]

        if name in friends:
            friends[friends.index(name)] = "Blacklisted"
            print(f'{name} was blacklisted.')
        else:
            print(f'{name} was not found.')

    elif command[0] == 'Error':
        index = int(command[1])
        if index in range(0, len(friends)) and friends[index] not in ['Blacklisted', 'Lost']:
            name = friends[index]
            print(f'{name} was lost due to an error.')
            friends[index] = 'Lost'

    elif command[0] == 'Change':
        index = command[1]
        new_name = command[2]
        index = int(index)

        if index in range(0, len(friends)):
            current_name = friends[index]
            friends[index] = new_name
            print(f'{current_name} changed his username to {new_name}.')

    command = input()

blacklisted = len([name for name in friends if name == 'Blacklisted'])
lost = len([name for name in friends if name == 'Lost'])

print(f'Blacklisted names: {blacklisted}')
print(f'Lost names: {lost}')
print(*friends, sep=" ")
