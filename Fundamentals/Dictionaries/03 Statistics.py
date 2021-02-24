command = input()
products = {}
while command != "statistics":
    items = command.split(": ")
    key = items[0]
    value = int(items[1])
    if products.get(key):
        products[key] += value
    else:
        products[key] = value
    command = input()
print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")

