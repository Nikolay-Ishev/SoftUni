from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]
total_time = 0
while taxis and customers:
    current_taxi = taxis[-1]
    current_customer = customers[0]
    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()
if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
