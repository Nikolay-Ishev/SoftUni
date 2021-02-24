def urgent(item):
    if item not in shopping_list:
        shopping_list.insert(0, item)


def unnecessary(item):
    while item in shopping_list:
        shopping_list.remove(item)


def correct(old_item, new_item):
    if old_item in shopping_list:
        shopping_list[shopping_list.index(old_item)] = new_item


def rearrange(item):
    if item in shopping_list:
        shopping_list.pop(shopping_list.index(item)) and shopping_list.append(item)


shopping_list = input().split("!")
command = input()
while command != "Go Shopping!":
    command = command.split()
    if command[0] == "Urgent":
        urgent(command[1])
    elif command[0] == "Unnecessary":
        unnecessary(command[1])
    elif command[0] == "Correct":
        correct(command[1], command[2])
    elif command[0] == "Rearrange":
        rearrange(command[1])
    command = input()

print(", ".join(shopping_list))



