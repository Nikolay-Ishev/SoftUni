command = input()
phonebook = {}
while not command.isdigit():
    if command[0].isalpha():
        name, number = command.split("-")
    else:
        number, name = command.split("-")
    phonebook[name] = number
    command = input()
for i in range(int(command)):
    search = input()
    if search not in phonebook:
        print(f"Contact {search} does not exist.")
    else:
        print(f"{search} -> {phonebook[search]}")



