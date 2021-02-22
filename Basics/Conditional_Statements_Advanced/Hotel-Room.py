month = str(input())
nights = int(input())
if (nights > 14 and month == "May") or (nights > 14 and month == "October"):
    print(f"Apartment: {((nights * 65) - (0.1 * (nights * 65))):.2f} lv.")
    print(f"Studio: {((nights * 50) - (0.3 * (nights * 50))):.2f} lv.")
elif (nights > 14 and month == "June") or (nights > 14 and month == "September"):
    print(f"Apartment: {((nights * 68.7) - (0.1 * (nights * 68.7))):.2f} lv.")
    print(f"Studio: {((nights * 75.2) - (0.2 * (nights * 75.2))):.2f} lv.")
elif nights > 14:
    print(f"Apartment: {((nights * 77) - (0.1 * (nights * 77))):.2f} lv.")
    print(f"Studio: {(nights * 76):.2f} lv.")
elif (nights > 7 and month == "May") or (nights > 7 and month == "October"):
    print(f"Apartment: {(nights * 65):.2f} lv.")
    print(f"Studio: {((nights * 50) - (0.05 * (nights * 50))):.2f} lv.")
elif month == "May" or month == "October":
    print(f"Apartment: {(nights * 65):.2f} lv.")
    print(f"Studio: {(nights * 50):.2f} lv.")
elif month == "June" or month == "September":
    print(f"Apartment: {(nights * 68.7):.2f} lv.")
    print(f"Studio: {(nights * 75.2):.2f} lv.")
elif month == "July" or month == "August":
    print(f"Apartment: {(nights * 77):.2f} lv.")
    print(f"Studio: {(nights * 76):.2f} lv.")
