from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()
command = input()
crash = False
total_cars_passed = 0
while command != "END" or crash:
    if command != "green":
        cars.append(command)
        command = input()
    else:
        green_light = green_light_duration
        free_window = free_window_duration
        if not cars:
            command = input()
            continue
        car_name = cars[0]
        car = deque(cars.popleft())
        while green_light > 0 or crash:
            if not car:
                if cars:
                    car_name = cars[0]
                    car = deque(cars.popleft())
                    car.popleft()
                    if not car:
                        total_cars_passed += 1
                else:
                    command = input()
                    break
            else:
                car.popleft()
                if not car:
                    total_cars_passed += 1
            green_light -= 1
        if car:
            while free_window > 0:
                free_window -= 1
                if car:
                    car.popleft()
            if car:
                print(f"A crash happened!")
                print(f"{car_name} was hit at {car[0]}.")
                crash = True
                break
            else:
                total_cars_passed += 1
            command = input()
if not crash:
    print(f"Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
