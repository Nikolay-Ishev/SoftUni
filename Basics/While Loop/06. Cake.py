width = int(input())
length = int(input())
cake = width * length
while cake >= 0:
    piece = input()
    if piece == "STOP":
        print(f"{cake} pieces are left.")
        break
    else:
        cake -= int(piece)
if cake < 0:
    print(f"No more cake left! You need {- cake} pieces more.")
