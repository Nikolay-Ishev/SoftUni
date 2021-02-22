# Пъзел - 2.60 лв.
# Говореща кукла - 3 лв.
# Плюшено мече - 4.10 лв.
# Миньон - 8.20 лв.
# Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът, прави отстъпка 25% от общата цена. От спечелените
# пари Петя трябва да даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на
# екскурзия.
# Вход
# От конзолата се четат 6 реда:
# 1. Цена на екскурзията - реално число;
# 2. Брой пъзели - цяло число;
# 3. Брой говорещи кукли - цяло число;
# 4. Брой плюшени мечета - цяло число;
# 5. Брой миньони - цяло число;
# 6. Брой камиончета - цяло число.

vacation_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
full_sum = (puzzles * 2.6) + (dolls * 3) + (bears * 4.1) + (minions * 8.2) + (trucks * 2)
toys = puzzles + dolls + bears + minions + trucks
if toys >= 50:
    real_sum = full_sum - (0.25 * full_sum)
    total_income = real_sum - (0.1 * real_sum)
    money = total_income - vacation_price
    minus_sum = vacation_price - total_income
# Ako парите са достатъчни се отпечатва:
# "Yes! {оставащите пари} lv left." ;
# Ако парите НЕ са достатъчни се отпечатва:
# "Not enough money! {недостигащите пари} lv needed."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

    if total_income >= vacation_price:
        print(f"Yes! {money:.2f} lv left.")
    else:
        print(f"Not enough money! {minus_sum:.2f} lv needed.")
else:
    the_income = full_sum - (0.1 * full_sum)
    the_money = the_income - vacation_price
    the_minus_sum = vacation_price - the_income
    if the_income >= vacation_price:
        print(f"Yes! {the_money:.2f} lv left.")
    else:
        print(f"Not enough money! {the_minus_sum:.2f} lv needed.")




