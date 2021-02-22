town = str(input())
sales = float(input())
commission = 0
if town == "Sofia":
    if 0 <= sales <= 500:
        commission += 0.05
        print(f"{(sales * commission):.2f}")
    elif 500 < sales <= 1000:
        commission += 0.07
        print(f"{(sales * commission):.2f}")
    elif 1000 < sales <= 10000:
        commission += 0.08
        print(f"{(sales * commission):.2f}")
    elif sales > 10000:
        commission += 0.12
        print(f"{(sales * commission):.2f}")
    else:
        print("error")
elif town == "Varna":
    if 0 <= sales <= 500:
        commission += 0.045
        print(f"{(sales * commission):.2f}")
    elif 500 < sales <= 1000:
        commission += 0.075
        print(f"{(sales * commission):.2f}")
    elif 1000 < sales <= 10000:
        commission += 0.1
        print(f"{(sales * commission):.2f}")
    elif sales > 10000:
        commission += 0.13
        print(f"{(sales * commission):.2f}")
    else:
        print("error")
elif town == "Plovdiv":
    if 0 <= sales <= 500:
        commission += 0.055
        print(f"{(sales * commission):.2f}")
    elif 500 < sales <= 1000:
        commission += 0.08
        print(f"{(sales * commission):.2f}")
    elif 1000 < sales <= 10000:
        commission += 0.12
        print(f"{(sales * commission):.2f}")
    elif sales > 10000:
        commission += 0.145
        print(f"{(sales * commission):.2f}")
    else:
        print("error")
else:
    print("error")
