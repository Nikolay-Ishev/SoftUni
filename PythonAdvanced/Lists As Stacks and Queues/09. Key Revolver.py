from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
value = int(input())
current_barrel = barrel_size
success = False
while bullets and locks:
    if current_barrel == 0:
        print("Reloading!")
        current_barrel = barrel_size
    bullet = bullets.pop()
    current_barrel -= 1
    value -= bullet_price
    lock = locks[0]
    if bullet <= lock:
        print("Bang!")
        locks.popleft()
        if not locks:
            success = True
        if current_barrel == 0 and len(bullets) > 0:
            print("Reloading!")
            current_barrel = barrel_size
    else:
        print("Ping!")
        continue
if success:
    if value < 0:
        value = 0
    print(f"{len(bullets)} bullets left. Earned ${value}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")


