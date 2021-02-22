strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())
raspberries_price = strawberries_price / 2
#цената на  малините е на половина по-ниска от тази на ягодите
#цената на портокалите е с 40% по-ниска от цената на малините
#цената на бананите е с 80% по-ниска от цената на малините

price = (strawberries_kg * strawberries_price) + (raspberries_price * raspberries_kg) + ((raspberries_price - 0.4 * raspberries_price) * oranges_kg) + ((raspberries_price - 0.8 * raspberries_price) * bananas_kg)
print(price)
print(f"{price:.2f}")


