parenthesis = input()
balance = True
pattern = {"{": "}", "(": ")", "[": "]"}
open_list = []
for el in parenthesis:
    if el in "{[(":
        open_list.append(el)
    else:
        if not open_list:
            balance = False
            break
        if el != pattern[open_list.pop()]:
            balance = False
            break
if balance:
    print("YES")
else:
    print("NO")
