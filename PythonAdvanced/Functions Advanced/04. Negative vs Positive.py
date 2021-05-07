neg = []
pos = []
for num in [int(x) for x in input().split()]:
    if num < 0:
        neg.append(num)
    else:
        pos.append(num)
print(sum(neg))
print(sum(pos))
if abs(sum(neg)) > sum(pos):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
