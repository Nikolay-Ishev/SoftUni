numbers = [int(x) for x in input().split(", ")]
positive = []
negative = []
even = []
odd = []
for n in numbers:
    if n >= 0:
        positive.append(n)
    else:
        negative.append(n)
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print(f"Positive: {', '.join([str(x) for x in positive])}")
print(f"Negative: {', '.join([str(x) for x in negative])}")
print(f"Even: {', '.join([str(x) for x in even])}")
print(f"Odd: {', '.join([str(x) for x in odd])}")
