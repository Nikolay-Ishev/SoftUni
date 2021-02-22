month = input()
hours = int(input())
people = int(input())
time = input()

# Март до Май       Юни до Август
# Ден 10.50 лв/ч    12.60 лв/ч
# Нощ 8.40 лв/ч     10.20 лв/ч
# Предлагат се и следните отстъпки в следната последователност:
# • За група от четирима или повече човека, цената на човек се намаля с 10%
# • За 5 или повече часа прекарани, цената на човек се намаля с 50%
#"march", "april", "may", "june", "july", "august"
# Да се отпечатат на конзолата 2 реда:
# • На първия ред: "Price per person for one hour: {цена на човек за час}"
# • На втория ред: "Total cost of the visit: {общата цена}"
# Цените да бъдат закръглени до втория знак след десетичната запетая

if month == "march" or month == "april" or month == "may":
    if time == "day":
        price = 10.50
    elif time == "night":
        price = 8.40
else:
    if time == "day":
        price = 12.60
    elif time == "night":
        price = 10.20
if people >= 4:
    price -= 0.1 * price
if hours >= 5:
    price -= 0.5 * price
print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {price * people * hours:.2f}")
