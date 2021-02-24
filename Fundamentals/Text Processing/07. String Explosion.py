str_1 = input()
expl = 0
for i in range(len(str_1)):
    if i > len(str_1) - 1:
        break
    if str_1[i] == '>':
        expl += int(str_1[i + 1])
        while str_1[i + 1] != ">" and expl > 0:
            expl -= 1
            str_1 = str_1[:(i + 1)] + str_1[i + 2:]
            if i >= len(str_1) - 1:
                break

print(str_1)

