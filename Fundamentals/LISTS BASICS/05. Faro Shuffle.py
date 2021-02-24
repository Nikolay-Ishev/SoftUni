card_list = [x for x in input().split(" ")]
shuffle_n = int(input())
for shuffle_number in range(shuffle_n):
    middle_list = card_list.copy()
    middle_list.pop(0) and middle_list.pop(-1)
    middle_index = len(middle_list) // 2
    first_half = middle_list[:middle_index]
    second_half = middle_list[middle_index:]
    first_half_check = False
    shuffle_list = []
    for shuffle in range(len(card_list)):
        if shuffle == 0:
            shuffle_list.append(card_list[0])
            continue
        elif shuffle == (len(card_list) - 1):
            shuffle_list.append(card_list[-1])
            continue
        if first_half_check:
            shuffle_list.append(first_half[0])
            first_half.pop(0)
            first_half_check = False
            continue
        else:
            shuffle_list.append(second_half[0])
            second_half.pop(0)
            first_half_check = True
            continue
    card_list = shuffle_list.copy()
print(card_list)



