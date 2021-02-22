degrees = int(input())
daytime = str(input())
if 10 <= degrees <= 18 and daytime == "Morning":
    outfit = "Sweatshirt"
    shoes = "Sneakers"
elif 10 <= degrees <= 18 and daytime == "Afternoon":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 10 <= degrees <= 18 and daytime == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 18 < degrees <= 24 and daytime == "Morning":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 18 < degrees <= 24 and daytime == "Afternoon":
    outfit = "T-Shirt"
    shoes = "Sandals"
elif 18 < degrees <= 24 and daytime == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
elif degrees >= 25 and daytime == "Morning":
    outfit = "T-Shirt"
    shoes = "Sandals"
elif degrees >= 25 and daytime == "Afternoon":
    outfit = "Swim Suit"
    shoes = "Barefoot"
elif degrees >= 25 and daytime == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
