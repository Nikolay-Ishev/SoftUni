deposit = float(input())
months = int(input())
y_interest = float(input())
sum1 = deposit + months * ((deposit * (y_interest / 100) / 12))
print(f"{sum1:.2f}")
print(sum1)



