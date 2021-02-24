n = int(input())
capacity = 255
for litters in range(n):
    liters = int(input())
    if liters > capacity:
        print("Insufficient capacity!")
        continue
    else:
        capacity -= liters
print(f"{255 - capacity}")


