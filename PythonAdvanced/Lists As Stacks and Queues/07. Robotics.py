from collections import deque
from datetime import datetime, timedelta

data = input().split(";")
robots = deque()
available_robots = deque()
time = datetime.strptime(input(), "%H:%M:%S")

for robot in data:
    r = {}
    r_name, r_process_time = robot.split("-")
    r["name"] = r_name
    r["processing_time"] = int(r_process_time)
    r["available"] = time
    robots.append(r)
    available_robots.append(r)

products = deque()
command = input()
while command != "End":
    products.append(command)
    command = input()

time = time + timedelta(seconds=1)

while products:
    current_product = products.popleft()
    if not available_robots:
        for r in robots:
            if time >= r["available"]:
                available_robots.append(r)
    if available_robots:
        current_robot = available_robots.popleft()
        current_robot["available"] = time + timedelta(seconds=current_robot["processing_time"])
        robot = [el for el in robots if el == current_robot][0]
        robot["available"] = time + timedelta(seconds=current_robot["processing_time"])
        print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        products.append(current_product)

    time = time + timedelta(seconds=1)
