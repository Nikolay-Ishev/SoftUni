user_name = input()
command = input()
while command != "Sign up":
    command = command.split()
    if command[0] == "Case":
        if command[1] == "lower":
            user_name = user_name.lower()
        elif command[1] == "upper":
            user_name = user_name.upper()
        print(user_name)
    elif command[0] == "Reverse":
        start_i, end_i = int(command[1]), int(command[2])
        if 0 <= start_i < len(user_name) and 0 <= end_i < len(user_name):
            substring = (user_name[start_i: 1 + end_i])[::-1]
            print(substring)
    elif command[0] == "Cut":
        substring = command[1]
        if substring in user_name:
            user_name = user_name.replace(substring, "")
            print(user_name)
        else:
            print(f"The word {user_name} doesn't contain {substring}.")
    elif command[0] == "Replace":
        char = command[1]
        user_name = user_name.replace(char, "*")
        print(user_name)
    elif command[0] == "Check":
        char = command[1]
        if char in user_name:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
    command = input()
