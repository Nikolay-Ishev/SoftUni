n = int(input())
pieces = {}
for data in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = [composer, key]
command = input()
while command != "Stop":
    command = command.split("|")
    if command[0] == "Add":
        piece, composer, key = command[1], command[2], command[3]
        if piece not in pieces:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in pieces:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece, new_key = command[1], command[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
pieces_ord = dict(sorted(pieces.items(), key = lambda x: (x[0], x[1][0])))
for key, value in pieces_ord.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
