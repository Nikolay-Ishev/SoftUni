message = input()
command = input()
while command != "Decode":
    instruction = command.split("|")
    if instruction[0] == "Move":
        n = int(instruction[1])
        message = message[n:] + message[:n]
    elif instruction[0] == "Insert":
        index, value = int(instruction[1]), instruction[2]
        message = message[:index] + value + message[index:]
    elif instruction[0] == "ChangeAll":
        substring, replacement = instruction[1], instruction[2]
        message = message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {message}")
