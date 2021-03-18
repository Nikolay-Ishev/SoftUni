clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_rack_capacity = rack_capacity
total_racks = 1
while clothes:
    if clothes[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes.pop()
    else:
        total_racks += 1
        current_rack_capacity = rack_capacity
print(total_racks)
