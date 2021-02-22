age = int(input())
wm_price = float(input())
t_price = int(input())
even = 0
odd = 0
diff = 0
for birthdays in range(1, age + 1):
    if birthdays % 2 == 0:
        diff += 10
        even += diff
    else:
        odd += t_price
for steals in range(1, age+1):
    if steals % 2 == 0:
        even -= 1
if even + odd >= wm_price:
    print(f"Yes! {(even + odd - wm_price):.2f}")
else:
    print(f"No! {(wm_price - even - odd):.2f}")








# Изход
# Да се отпечата на конзолата един ред:
# Ако парите на Лили са достатъчни:
# o"Yes! {N}" - където N е остатъка пари след покупката
# Ако парите не са достатъчни:
# o"No! {М}" - където M е сумата, която не достига
# Числата N и M трябва да за форматирани до вторият знак след десетичната запетая.