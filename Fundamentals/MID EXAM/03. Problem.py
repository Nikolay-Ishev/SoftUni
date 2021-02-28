cards = input().split(":")
command = input()
deck = []
while command != "Ready":
    command = command.split()
    if command[0] == "Add":
        card = command[1]
        if card not in cards:
            print("Card not found.")
        else:
            deck.append(card)
    elif command[0] == "Insert":
        card = command[1]
        index = int(command[2])
        if card not in cards or index not in range(len(deck)):
            print("Error!")
        else:
            deck.insert(index, card)
    elif command[0] == "Remove":
        card = command[1]
        if card not in deck:
            print("Card not found.")
        else:
            deck.remove(card)
    elif command[0] == "Swap":
        card_1 = command[1]
        card_2 = command[2]
        i_1 = deck.index(card_1)
        i_2 = deck.index(card_2)
        deck[i_1], deck[i_2] = deck[i_2], deck[i_1]
    elif command[0] == "Shuffle":
        deck.reverse()
    command = input()
print(*deck, sep=" ")



