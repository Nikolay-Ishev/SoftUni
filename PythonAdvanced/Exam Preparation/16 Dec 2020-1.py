from collections import deque


males_list = [int(x) for x in input().split()]
females_queue = deque(int(x) for x in input().split())
matches = 0
while males_list and females_queue:
    # special cases
    if females_queue[0] <= 0:
        females_queue.popleft()
        continue
    if males_list[-1] <= 0:
        males_list.pop()
        continue
    if females_queue[0] % 25 == 0:
        females_queue.popleft()
        females_queue.popleft()
        continue
    if males_list[-1] % 25 == 0:
        males_list.pop()
        males_list.pop()
        continue
    # main case
    if females_queue[0] == males_list[-1]:
        males_list.pop()
        females_queue.popleft()
        matches += 1
    else:
        females_queue.popleft()
        males_list[-1] -= 2
if males_list:
    males_list = ", ".join(str(x) for x in males_list[::-1])
else:
    males_list = "none"
if females_queue:
    females_queue = ", ".join(str(x) for x in females_queue)
else:
    females_queue = "none"
print(f"Matches: {matches}")
print(f"Males left: {males_list}")
print(f"Females left: {females_queue}")
