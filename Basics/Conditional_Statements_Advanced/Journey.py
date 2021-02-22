budget = float(input())
season = str(input())
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        holiday = "Camp"
        price = 0.3 * budget
    elif season == "winter":
        holiday = "Hotel"
        price = 0.7 * budget
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        holiday = "Camp"
        price = 0.4 * budget
    elif season == "winter":
        holiday = "Hotel"
        price = 0.8 * budget
else:
    destination = "Europe"
    holiday = "Hotel"
    price = 0.9 * budget
print(f"Somewhere in {destination}")
print(f"{holiday} - {price:.2f}")
