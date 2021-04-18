def rounding(collection):
    abs_v = []
    for n in collection:
        abs_v.append(round(n))
    return abs_v


numbers = [float(x) for x in input().split()]
print(rounding(numbers))
