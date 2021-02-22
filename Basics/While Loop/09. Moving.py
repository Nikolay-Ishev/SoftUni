width = int(input())
length = int(input())
height = int(input())
size = width * length * height
box = input()
box_sum = 0
while box != "Done":
    box_sum += int(box)
    if box_sum <= size:
        box = input()
    else:
        print(f"No more free space! You need {box_sum - size} Cubic meters more.")
        break
if box_sum <= size:
    print(f"{size - box_sum} Cubic meters left.")
