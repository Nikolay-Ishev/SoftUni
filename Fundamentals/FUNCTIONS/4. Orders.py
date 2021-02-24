#  coffee - 1.50
#  water - 1.00
#  coke - 1.40
#  snacks - 2.00

product_input = input()
product_quantity = int(input())


def total_price(product, quantity):
    price = 0
    if product == "coffee":
        price = quantity * 1.5
    elif product == "water":
        price = quantity * 1
    elif product == "coke":
        price = quantity * 1.4
    elif product == "snacks":
        price = quantity * 2
    return f"{price:.2f}"


print(total_price(product_input, product_quantity))
