command = input()
products = {}
while command != "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products[name] = [0, 0]
    if products[name][0] != price:
        products[name][0] = price
    products[name][1] += quantity
    command = input()
for key, value in products.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")







