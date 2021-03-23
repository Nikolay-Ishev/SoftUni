n = int(input())
cars = set()
for command in range(n):
    action, car = input().split(", ")
    if action == "IN":
        cars.add(car)
    else:
        cars.remove(car)
if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
