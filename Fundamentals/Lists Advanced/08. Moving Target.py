target_list = input().split()
target_list = [int(x) for x in target_list]
command = input().split()
while command[0] != "End":
    index = int(command[1])
    if command[0] == 'Shoot':
        if len(target_list) < index + 1 or index < 0:
            command = input().split()
            continue
        target_list[index] -= int(command[2])
        if target_list[index] <= 0:
            target_list.pop(index)
    elif command[0] == 'Add':
        if len(target_list) < index + 1 or index < 0:
            print("Invalid placement!")
        else:
            target_list.insert(index, int(command[2]))
    elif command[0] == "Strike":
        if int(command[2]) > index or (int(command[2]) + index) > len(target_list) - 1 or index < 0:
            print("Strike missed!")
        else:
            del target_list[index - int(command[2]):index + int(command[2]) + 1]
    command = input().split()
target_list = [str(x) for x in target_list]
print('|'.join(target_list))





