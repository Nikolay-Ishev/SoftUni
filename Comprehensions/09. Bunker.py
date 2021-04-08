categories = input().split(", ")
bunker = {x: {} for x in categories}
total_quantity = 0
total_quality = 0
for i in range(int(input())):
    command = input()
    category, name, info = command.split(" - ")
    quantity, quality = info.split(";")
    quantity = int(quantity[9:])
    quality = int(quality[8:])
    bunker[category][name] = [quantity, quality]
    total_quality += quality
    total_quantity += quantity
print(f"Count of items: {total_quantity}")
print(f"Average quality: {total_quality / len(bunker):.2f}")
for key, value in bunker.items():
    print(f"{key} -> {', '.join(x for x in value)}")
