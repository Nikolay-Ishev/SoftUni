#един кв. м. е 7.61лв със ДДС, 18% отстъпка от крайната цена
green_area = float(input())
sum1 = green_area * 7.61
discount = 0.18 * sum1
price = sum1 - discount
print(f"The final price is: {price:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")

# закръгляне до определен знак - :.2f
# print(f"{price:.2f}")
