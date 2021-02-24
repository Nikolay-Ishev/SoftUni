import re

pattern = r"(?<=\b_)[A-Za-z0-9]+\b"
data = input()
matches = re.findall(pattern, data)
print(*matches, sep=",")
