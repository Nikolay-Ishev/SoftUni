import re

pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>\d+|(\d+\.\d+))!(?P<quantity>\d+)"
command = input()
furniture = []
price = 0
while command != "Purchase":
    string = re.finditer(pattern, command)
    for el in string:
        d = el.groupdict()
        furniture.append(d["name"])
        price += float(d["price"]) * int(d["quantity"])
    command = input()
print("Bought furniture:")
for el in furniture:
    print(el)
print(f'Total money spend: {price:.2f}')
