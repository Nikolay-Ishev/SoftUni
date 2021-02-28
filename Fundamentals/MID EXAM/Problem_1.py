n = int(input())
total_price = 0
for order in range(n):
    capsule_price = float(input())
    days = int(input())
    capsules = int(input())
    price = (days * capsules) * capsule_price
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
