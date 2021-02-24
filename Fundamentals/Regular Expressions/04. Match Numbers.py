import re

data = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, data)
matches = [n.group() for n in matches]
# print(" ".join(matches))
print(*matches)
