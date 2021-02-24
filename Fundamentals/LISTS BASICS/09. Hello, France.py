item_list = input().split("|")
budget = float(input())
total_profit = 0
new_price_total = 0
for item in item_list:
    item_type, price = item.split("->")
    price = float(price)
# Type	Maximum Price
# Clothes	50.00
# Shoes	35.00
# Accessories	20.50
    if item_type == "Clothes" and price > 50:
        continue
    elif item_type == "Shoes" and price > 35:
        continue
    elif item_type == "Accessories" and price > 20.5:
        continue
    if budget < price:
        continue
    budget -= price
    new_price = 1.4 * price
    new_price_total += new_price
    total_profit += 0.4 * price
    print(f"{new_price:.2f}", end=" ")
print()
print(f"Profit: {total_profit:.2f}")
if budget + new_price_total >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
