budget = float(input())
product = input()
products_count = 0
price_total = 0
while product != "Stop":
    price = float(input())
    products_count += 1
    if products_count % 3 == 0:
        price = 0.5 * price
    if price <= budget:
        budget -= price
        price_total += price
    elif price >= budget:
        break
    product = input()
if product == "Stop":
    print(f"You bought {products_count} products for {price_total:.2f} leva.")
else:
    print(f"You don't have enough money!")
    print(f"You need {price - budget:.2f} leva!")
