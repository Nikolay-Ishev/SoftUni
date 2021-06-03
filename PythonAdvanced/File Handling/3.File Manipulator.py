import os

command = input().split("-")
while command[0] != "End":
    file_name = command[1]
    if command[0] == "Create":
        with open(file_name, "w") as file:
            command = input().split("-")
            continue
    elif command[0] == "Add":
        content = f"{command[2]}\n"
        with open(file_name, "a") as file:
            file.write(content)
    elif command[0] == "Replace":
        old_content = command[2]
        new_content = command[3]
        try:
            with open(file_name, "r+") as file:
                text = file.read()
                text = text.replace(old_content, new_content)
                file.seek(0)
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")
    elif command[0] == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
    command = input().split("-")
