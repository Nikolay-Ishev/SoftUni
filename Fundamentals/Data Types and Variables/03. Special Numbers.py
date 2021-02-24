number = int(input())
for n in range(1, number + 1):
    sum_d = 0
    for i in range(len(str(n))):
        sum_d += int(str(n)[i])
    if sum_d == 5 or sum_d == 7 or sum_d == 11:
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")


