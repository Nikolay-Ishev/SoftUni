rooms = int(input())
free_chairs = 0
Game_on = True
for room in range(1, rooms + 1):
    chair_list = input().split()
    if len(chair_list[0]) < int(chair_list[1]):
        print(f"{int(chair_list[1]) - len(chair_list[0])} more chairs needed in room {room}")
        Game_on = False
    else:
        free_chairs += len(chair_list[0]) - int(chair_list[1])
if Game_on:
    print(f"Game On, {free_chairs} free chairs left")
