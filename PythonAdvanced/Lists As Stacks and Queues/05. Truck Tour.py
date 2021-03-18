from collections import deque

n_pumps = int(input())
stations = deque()
for pump in range(n_pumps):
    stations.append(input())
for starting_point in range(n_pumps):
    total_petrol = 0
    temporary_stations = stations.copy()
    success = True
    while temporary_stations:
        current_station = temporary_stations.popleft()
        petrol, distance = current_station.split()
        petrol = int(petrol)
        distance = int(distance)
        total_petrol += petrol
        if total_petrol < distance:
            success = False
            stations.append(stations.popleft())
            break
        else:
            total_petrol -= distance
    if success:
        print(starting_point)
        break
