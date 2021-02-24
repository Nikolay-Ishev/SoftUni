import re


data = input()
pattern = r"\d+"
numbers = []
while data:
    match = re.findall(pattern, data)
    if match:
        numbers.extend(match)
    data = input()
print(*numbers, sep=" ")


