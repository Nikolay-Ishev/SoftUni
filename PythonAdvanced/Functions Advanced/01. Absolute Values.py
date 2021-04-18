def absolute_value(collection):
    abs_v = []
    for n in collection:
        abs_v.append(abs(n))
    return abs_v


numbers = [float(x) for x in input().split()]
print(absolute_value(numbers))
