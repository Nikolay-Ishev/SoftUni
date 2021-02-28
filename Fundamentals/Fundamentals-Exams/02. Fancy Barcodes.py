import re

pattern = r"@#+[A-Z][0-9a-zA-Z]{4,}[A-Z]@#+"
digit_pattern = r'\d+'
n = int(input())
for i in range(n):
    barcode = input()
    x = re.findall(pattern, barcode)
    # може да се използва re.match
    #  a = re.match(pattern, barcode)
    #  a.group()
    if not x:
        print("Invalid barcode")
    else:
        barcode = x[0]
        pr_group = re.findall(digit_pattern, barcode)
        if not pr_group:
            pr_group = "00"
        else:
            pr_group = "".join(pr_group)
        print(f"Product group: {pr_group}")

