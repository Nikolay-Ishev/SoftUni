def take_odd(p):
    new_password = ""
    for x in range(len(p)):
        if x % 2 != 0:
            new_password += p[x]
    return new_password


def cut(p, index, length):
    new_password = p[:index] + p[index + length:]
    return new_password


def substitude(p, substring, substitute):
    if substring in p:
        new_password = p.replace(substring, substitute)
        print(new_password)
        return new_password
    else:
        print("Nothing to replace!")
        return p


password = input()
command = input()
while command != "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        password = take_odd(password)
        print(password)
    elif command[0] == "Cut":
        password = cut(password, int(command[1]), int(command[2]))
        print(password)
    elif command[0] == "Substitute":
        password = substitude(password, command[1], command[2])
    command = input()
print(f"Your password is: {password}")
