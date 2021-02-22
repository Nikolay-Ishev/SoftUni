number = float(input())
metric = str(input())
convert_to = str(input())
if metric == "m":
    if convert_to == "cm":
        result = number * 100
        print(f"{result:.3f}")
    elif convert_to == "mm":
        result = number * 1000
        print(f"{result:.3f}")
elif metric == "cm":
    if convert_to == "m":
        result = number / 100
        print(f"{result:.3f}")
    elif convert_to == "mm":
        result = number * 10
        print(f"{result:.3f}")
elif metric == "mm":
    if convert_to == "cm":
        result = number / 10
        print(f"{result:.3f}")
    elif convert_to == "m":
        result = number / 1000
        print(f"{result:.3f}")








