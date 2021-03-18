from collections import deque

f_quantity = int(input())
orders = input().split()
orders = deque([int(x) for x in orders])
print(max(orders))
while orders:
    if orders[0] <= f_quantity:
        f_quantity -= orders.popleft()
    else:
        orders_left = " ".join([str(x) for x in orders])
        print(f"Orders left: {orders_left}")
        break
if not orders:
    print("Orders complete")
