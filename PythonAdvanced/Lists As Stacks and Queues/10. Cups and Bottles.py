from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_litters = 0

while cups and bottles:
    bottle = bottles.pop()
    cups[0] -= bottle
    if cups[0] > 0:
        continue
    else:
        waste = 0 - cups[0]
        wasted_litters += waste
        cups.popleft()
if cups:
    cups_str = " ".join([str(x) for x in cups])
    print(f"Cups: {cups_str} ")
else:
    bottles_str = " ".join([str(x) for x in bottles])
    print(f"Bottles: {bottles_str}")
print(f"Wasted litters of water: {wasted_litters}")
