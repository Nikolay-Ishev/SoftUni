flower_type = str(input())
flower_amount = int(input())
budget = int(input())
final_price = 0
if flower_type == "Roses":
    price = 5 * flower_amount
    if flower_amount > 80:
        final_price = price - (0.1 * price)
    else:
        final_price = price
elif flower_type == "Dahlias":
    price = 3.8 * flower_amount
    if flower_amount > 90:
        final_price = price - (0.15 * price)
    else:
        final_price = price
elif flower_type == "Tulips":
    price = 2.8 * flower_amount
    if flower_amount > 80:
        final_price = price - (0.15 * price)
    else:
        final_price = price
elif flower_type == "Narcissus":
    price = 3 * flower_amount
    if flower_amount < 120:
        final_price = price + (0.15 * price)
    else:
        final_price = price
elif flower_type == "Gladiolus":
    price = 2.5 * flower_amount
    if flower_amount < 80:
        final_price = price + (0.2 * price)
    else:
        final_price = price
if budget >= final_price:
    print(f"Hey, you have a great garden with {flower_amount} {flower_type} and {(budget - final_price):.2f} leva left.")
else:
    print(f"Not enough money, you need {(final_price - budget):.2f} leva more.")

