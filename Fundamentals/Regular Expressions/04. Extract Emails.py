import re

data = input()
pattern = r"(^|(?<=\s))[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+@[a-zA-Z]+-?[a-zA-Z]+(\.[a-zA-Z]+-?[a-zA-Z]+)+"
result = re.finditer(pattern, data)
[print(n.group()) for n in result]




