days = int(input())
candymen = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

#Торта - 45 лв.,     Гофрета - 5.80 лв.,    Палачинка – 3.20 лв.

money = candymen * (cakes * 45 + waffles * 5.8 + pancakes * 3.2) * days
expenses = 1 / 8 * money
final_price = money - expenses
print(final_price)
