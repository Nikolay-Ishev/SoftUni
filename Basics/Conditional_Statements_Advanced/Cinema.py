screen_type = str(input())
rows = int(input())
columns = int(input())
price = 0
if screen_type == "Premiere":
    price += 12
elif screen_type == "Normal":
    price += 7.5
elif screen_type == "Discount":
    price += 5
print(f"{(price * columns * rows):.2f}")
