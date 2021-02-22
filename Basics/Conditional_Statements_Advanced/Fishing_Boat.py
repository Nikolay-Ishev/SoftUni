budget = int(input())
season = str(input())
fishermen = int(input())
price = 0
if season == "Spring" and fishermen <= 6:
    price = 3000 - (0.1 * 3000)
    if fishermen % 2 == 0:
        final_price = price - (0.05 * price)
    else:
        final_price = price
elif season == "Spring" and 7 <= fishermen <= 11:
    price = 3000 - (0.15 * 3000)
    if fishermen % 2 == 0:
        final_price = price - (0.05 * price)
    else:
        final_price = price
elif season == "Spring" and fishermen > 11:
    price = 3000 - (0.25 * 3000)
    if fishermen % 2 == 0:
        final_price = price - (0.05 * price)
    else:
        final_price = price
elif season == "Summer" and fishermen <= 6:
    price = 4200 - (0.1 * 4200)
    if fishermen % 2 == 0:
        final_price = price - (0.05 * price)
    else:
        final_price = price
elif season == "Summer" and 7 <= fishermen <= 11:
    price = 4200 - (0.15 * 4200)
    if fishermen % 2 == 0:
        final_price = price - (0.05 * price)
    else:
        final_price = price
elif season == "Summer" and fishermen > 11:
    price = 4200 - (0.25 * 4200)
    if fishermen % 2 == 0:
        final_price = price - (0.05 * price)
    else:
        final_price = price
elif season == "Autumn" and fishermen <= 6:
    final_price = 4200 - (0.1 * 4200)
elif season == "Autumn" and 7 <= fishermen <= 11:
    final_price = 4200 - (0.15 * 4200)
elif season == "Autumn" and fishermen > 11:
    final_price = 4200 - (0.25 * 4200)
elif season == "Winter" and fishermen <= 6:
    price = 2600 - (0.1 * 2600)
    if fishermen % 2 == 0:
        final_price = price - (0.05 * price)
    else:
        final_price = price
elif season == "Winter" and 7 <= fishermen <= 11:
    price = 2600 - (0.15 * 2600)
    if fishermen % 2 == 0:
        final_price = price - (0.05 * price)
    else:
        final_price = price
elif season == "Winter" and fishermen > 11:
    price = 2600 - (0.25 * 2600)
    if fishermen % 2 == 0:
        final_price = price - (0.05 * price)
    else:
        final_price = price
if budget >= final_price:
    print(f"Yes! You have {(budget - final_price):.2f} leva left.")
else:
    print(f"Not enough money! You need {(final_price - budget):.2f} leva.")
