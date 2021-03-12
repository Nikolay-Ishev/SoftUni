from collections import deque

water = int(input())
command = input()
queue = deque()
while command != "Start":
    queue.append(command)
    command = input()
command = input()
while command != "End":
    if command.startswith("refill"):
        refill_water = int(command.split()[1])
        water += refill_water
    else:
        water_needed = int(command)
        person = queue.popleft()
        if water_needed <= water:
            water -= water_needed
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
    command = input()
print(f"{water} liters left")
