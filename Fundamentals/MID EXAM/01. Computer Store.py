total_price = 0
command = input()
while command != "special" and command != "regular":
    if float(command) <= 0:
        print("Invalid price!")
    else:
        total_price += float(command)
    command = input()
taxes = 0.2 * total_price
final_price = total_price + taxes
if final_price == 0:
    print("Invalid order!")
else:
    if command == "special":
        final_price -= 0.1 * final_price
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {final_price:.2f}$')
