from collections import deque

queue = deque(input().split())
counter = 0
toss = int(input())
while len(queue) != 1:
    counter += 1
    name = queue.popleft()
    if counter != toss:
        queue.append(name)
    else:
        print(f"Removed {name}")
        counter = 0
print(f"Last is {queue.popleft()}")
