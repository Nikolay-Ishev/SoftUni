gift_list = [str(x) for x in input().split(" ")]
command = input()
while command != "No Money":
    command_list = command.split(" ")
    if command_list[0] == "OutOfStock":
        for n, i in enumerate(gift_list):
            if i == command_list[1]:
                gift_list[n] = "None"
    elif command_list[0] == "Required":
        if 0 <= int(command_list[2]) <= len(gift_list) - 1:
            gift_list[int(command_list[2])] = command_list[1]
    elif command_list[0] == "JustInCase":
        gift_list[-1] = command_list[1]
    command = input()
#ТОВА НЕ РАБОТИ
# for e in gift_list:
#     if e == "None":
#         gift_list.remove(e)
while 'None' in gift_list:
    gift_list.remove('None')
print(" ".join(gift_list))



# "OutOfStock {gift}"
# oFind the gifts with this name in your collection, if there are any, and change their values to "None".
# "Required {gift} {index}"
# oReplace the value of the current gift on the given index with this gift, if the index is valid.
# "JustInCase {gift}"
# oReplace the value of your last gift with this one.
