budget = float(input())
price_flour = float(input())
# Here is the recipe for one cozonac:
# Eggs	1 pack
# Flour	1 kg
# Milk	0.250 l
# The price for 1 pack of eggs is 75% of the price for 1 kg flour.
# The price for 1l milk is 25% more than price for 1 kg flour. Notice, that you need 0.250l milk for one cozonac and the calculated price is for 1l.
# Start cooking the cozonacs and keep making them until you have enough budget. Keep in mind that:
# For every cozonac that you make, you will receive 3 colored eggs.
# For every 3rd cozonac that you make, you will lose some of your colored eggs after you have received the usual 3 colored eggs for your cozonac.
# The count of eggs you will lose is calculated when you subtract 2 from your current count of cozonacs – ({currentCozonacsCount} – 2)
# In the end, print the cozonacs you made, the eggs you have gathered and the money you have left, formatted to the 2nd decimal place,
# in the following format:
# "You made {countOfCozonacs} cozonacs! Now you have {coloredEggs} eggs and {moneyLeft}BGN left."
price_eggs = 0.75 * price_flour
price_milk = 0.25 * (price_flour + (0.25 * price_flour))
price_cozonac = price_flour + price_eggs + price_milk
cozonacs = 0
colored_eggs = 0
while budget >= price_cozonac:
    cozonacs += 1
    budget -= price_cozonac
    colored_eggs += 3
    if cozonacs % 3 == 0:
        colored_eggs -= cozonacs - 2
print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

